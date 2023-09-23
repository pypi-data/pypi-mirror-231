import pandas as pd
from datasets import load_dataset
from transformers import AutoTokenizer 
from pprint import pprint

def dataprep(model_name="", out_tokeniser="", dataset_name="", dataset_arg="", map_function=""):
    # Need one parameter for getting the tokenizer:
    if out_tokeniser:
        tokenizer = out_tokeniser
    else:
        tokenizer = AutoTokenizer.from_pretrained(model_name)

    # For downloading dataset
    if dataset_arg:
        dataset = dataset_arg
    else:
        dataset = load_dataset(dataset_name, split='train')

    # The function to be modified
    if map_function:
        tokenize_function = map_function
    else:
        def tokenize_function(examples):
            # Extract the column names from the dataset
            names = list(examples.keys())
            
            # Define a list to hold the concatenated text
            text = ""
            for name in names:
                text += examples[name][0]  # Concatenate the first item in each column
            
            tokenizer.pad_token = tokenizer.eos_token
            tokenize_inputs = tokenizer(
                text,
                return_tensors='np',
                padding=True
            )
            max_length = min(
                tokenize_inputs["input_ids"].shape[1], 2048
            )
            tokenizer.truncation_side = 'left'
            tokenise_inputs = tokenizer(
                text,
                return_tensors='np',
                truncation=True,
                max_length=max_length
            )
            return tokenise_inputs

    # Mapping
    tokenized_dataset = dataset.map(
        tokenize_function,
        batched=True,  # Enable batch processing
        batch_size=1,   # Set the batch size as needed
        drop_last_batch=True  # Drop the last batch if it's smaller than batch_size
    )

    # Adding labels
    tokenized_dataset = tokenized_dataset.add_column("labels", tokenized_dataset["input_ids"])
    
    return tokenized_dataset

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/pythia-70m")
def tokenize_function(examples):
            # Extract the column names from the dataset
            names = list(examples.keys())
            
            # Define a list to hold the concatenated text
            text = ""
            for name in names:
                text += examples[name][0]  # Concatenate the first item in each column
            
            tokenizer.pad_token = tokenizer.eos_token
            tokenize_inputs = tokenizer(
                text,
                return_tensors='np',
                padding=True
            )
            max_length = min(
                tokenize_inputs["input_ids"].shape[1], 2048
            )
            tokenizer.truncation_side = 'left'
            tokenise_inputs = tokenizer(
                text,
                return_tensors='np',
                truncation=True,
                max_length=max_length
            )
            return tokenise_inputs
data = dataprep(model_name="EleutherAI/pythia-70m", dataset_name="fka/awesome-chatgpt-prompts")
pprint(data)