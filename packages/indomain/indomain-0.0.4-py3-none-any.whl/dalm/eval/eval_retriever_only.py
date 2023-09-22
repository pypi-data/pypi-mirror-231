import argparse
import os
import sys

# ruff:noqa
from argparse import Namespace
from typing import Any, Dict, Final, List

import datasets
import numpy as np
import torch

from accelerate.logging import get_logger
from torch.utils.data import DataLoader
from tqdm import tqdm
from transformers import default_data_collator

from dalm.eval.utils import (
    calculate_precision_recall,
    construct_search_index,
    get_nearest_neighbours,
    preprocess_function,
    mixed_collate_fn,
)
from dalm.models.retriever_only_base_model import AutoModelForSentenceEmbedding

logger = get_logger(__name__)


def parse_args() -> Namespace:
    parser = argparse.ArgumentParser(description="Testing a PEFT model for Sematic Search task")
    parser.add_argument(
        "--dataset_path",
        type=str,
        default=None,
        help="dataset path in the local dir. Can be huggingface dataset directory or a csv file.",
        required=True,
    )
    parser.add_argument("--query_column_name", type=str, default="query", help="name of the query col")
    parser.add_argument(
        "--passage_column_name",
        type=str,
        default="passage",
        help="name of the passage col",
    )
    parser.add_argument("--embed_dim", type=int, default=1024, help="dimension of the model embedding")
    parser.add_argument(
        "--max_length",
        type=int,
        default=128,
        help=(
            "The maximum total input sequence length after tokenization. Sequences longer than this will be truncated,"
            " sequences shorter will be padded if `--pad_to_max_length` is passed."
        ),
    )
    parser.add_argument(
        "--retriever_name_or_path",
        type=str,
        help="Path to pretrained retriever model or model identifier from huggingface.co/models.",
        required=True,
    )
    parser.add_argument(
        "--retriever_peft_model_path",
        type=str,
        help="Path to the finetunned retriever peft layers",
        required=True,
    )
    parser.add_argument(
        "--test_batch_size",
        type=int,
        default=8,
        help="Batch size (per device) for the test dataloader.",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cuda",
        help="Device. cpu or cuda.",
    )
    parser.add_argument(
        "--torch_dtype",
        type=str,
        default="float16",
        help="torch.dtype to use for tensors. float16 or bfloat16.",
    )
    parser.add_argument(
        "--top_k",
        type=int,
        default=10,
        help="Top K retrieval",
    )
    parser.add_argument(
        "--evaluate_generator",
        action="store_true",
        help="Enable generator evaluation.",
    )
    args = parser.parse_args()

    return args


def main() -> None:
    args = parse_args()
    SELECTED_TORCH_DTYPE: Final[torch.dtype] = torch.float16 if args.torch_dtype == "float16" else torch.bfloat16

    # rag retriver and the generator (don't load new peft layers no need)
    retriever_model = AutoModelForSentenceEmbedding(args.retriever_name_or_path, get_peft=False, use_bnb=False)

    # load the test dataset
    test_dataset = (
        datasets.load_from_disk(args.dataset_path)
        if os.path.isdir(args.dataset_path)
        else datasets.load_dataset("csv", data_files={"test": f"{args.dataset_path}"})["test"]
    )

    # test_dataset = datasets.load_from_disk("/home/datasets/question_answer_pairs")

    retriever_tokenizer = retriever_model.tokenizer

    processed_datasets = test_dataset.map(
        lambda example: preprocess_function(
            example,
            retriever_tokenizer,
            query_column_name=args.query_column_name,
            passage_column_name=args.passage_column_name,
        ),
        batched=True,
        # remove_columns=test_dataset.column_names,
        desc="Running tokenizer on dataset",
        num_proc=4,
    )

    unique_passages = set(processed_datasets[args.passage_column_name])

    def is_passage_unique(example: Dict[str, Any]) -> bool:
        is_in_unique_list = example[args.passage_column_name] in unique_passages
        unique_passages.discard(example[args.passage_column_name])
        return is_in_unique_list

    unique_passage_dataset = processed_datasets.filter(is_passage_unique)

    passage_to_id_dict = {i: p[args.passage_column_name] for i, p in enumerate(unique_passage_dataset)}

    unique_passage_dataloader = DataLoader(
        unique_passage_dataset,
        shuffle=False,
        collate_fn=default_data_collator,
        batch_size=args.test_batch_size,
        pin_memory=True,
    )

    # peft config and wrapping
    retriever_model.attach_pre_trained_peft_layers(args.retriever_peft_model_path, args.device)

    def get_query_embeddings(
        retriever_query_input_ids: torch.Tensor,
        retriever_query_attention_masks: torch.Tensor,
    ) -> np.ndarray:
        return (
            retriever_model.forward(
                input_ids=retriever_query_input_ids.to(args.device),
                attention_mask=retriever_query_attention_masks.to(args.device),
            )
            .detach()
            .float()
            .cpu()
            .numpy()
        )

    def get_passage_embeddings(
        retriever_passage_input_ids: torch.Tensor,
        retriever_passage_attention_masks: torch.Tensor,
    ) -> np.ndarray:
        return (
            retriever_model.forward(
                input_ids=retriever_passage_input_ids.to(args.device),
                attention_mask=retriever_passage_attention_masks.to(args.device),
            )
            .detach()
            .float()
            .cpu()
            .numpy()
        )

    num_passages = len(unique_passage_dataset)
    print(f"Starting to generate passage embeddings (Number of passages: {num_passages})")

    passage_embeddings_array = np.zeros((num_passages, args.embed_dim))
    for step, batch in enumerate(tqdm(unique_passage_dataloader)):
        with torch.no_grad():
            with torch.amp.autocast(dtype=SELECTED_TORCH_DTYPE, device_type=args.device):
                passage_embs = get_passage_embeddings(
                    batch["retriever_passage_input_ids"],
                    batch["retriever_passage_attention_mask"],
                )

        start_index = step * args.test_batch_size
        end_index = (
            start_index + args.test_batch_size if (start_index + args.test_batch_size) < num_passages else num_passages
        )
        passage_embeddings_array[start_index:end_index] = passage_embs
        del passage_embs, batch

    print("Construct passage index")
    passage_search_index = construct_search_index(args.embed_dim, num_passages, passage_embeddings_array)

    # Initialize counters
    batch_precision = []
    batch_recall = []
    total_hit = 0

    print("Evaluation start")

    actual_length = len(processed_datasets)

    processed_datasets = DataLoader(
        processed_datasets, batch_size=args.test_batch_size, shuffle=True, collate_fn=mixed_collate_fn
    )

    # here we are interacting through the dataset, not a dataloader
    # so we need to convert them to a tensor
    # to do : convert this to batches by examples from the dataset to make it effcient
    # to:do : torch_dtype make a varaibles float16 or bfloat16
    for test_example in processed_datasets:
        with torch.no_grad():
            with torch.amp.autocast(dtype=SELECTED_TORCH_DTYPE, device_type=args.device):
                # use the batch size for the first dim
                # do not hard-code it
                retriever_query_input_ids = test_example["retriever_query_input_ids"]
                retriever_query__attention_mask = test_example["retriever_query_attention_mask"]

                query_embeddings = get_query_embeddings(
                    retriever_query_input_ids,
                    retriever_query__attention_mask,
                )

        search_results = get_nearest_neighbours(
            args.top_k,
            passage_search_index,
            query_embeddings,
            passage_to_id_dict,
            threshold=0.0,
        )

        correct_passages = test_example[args.passage_column_name]

        for i, s in enumerate(search_results):
            retrieved_passages = [item[0] for item in s]

            correct_passage = [correct_passages[i]]

            precision, recall = calculate_precision_recall(retrieved_passages, correct_passage)

            batch_precision.append(precision)
            batch_recall.append(recall)

            hit = any(passage in retrieved_passages for passage in correct_passage)
            total_hit += hit

    total_examples = actual_length
    recall = sum(batch_recall) / total_examples
    precision = sum(batch_precision) / total_examples
    hit_rate = total_hit / float(total_examples)

    print("Retriever results:")

    print("Recall:", recall)
    print("Precision:", precision)
    print("Hit Rate:", hit_rate)

    print("*************")


if __name__ == "__main__":
    main()
