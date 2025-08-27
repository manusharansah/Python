import json

FILE_NAME = "transactions.json"

def load_transactions():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_transactions(transactions):
    with open(FILE_NAME, "w") as f:
        json.dump(transactions, f, indent=4)
