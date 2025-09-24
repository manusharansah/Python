'''
Project Name: Personal Expense Tracker
'''

import json
from datetime import datetime

file_name = "transaction_details.json"

def load_transactions():
    try:
        with open(file_name,"r") as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return []
    

def view_transactions(transactions):
    if transactions:
        for x in transactions:
            print(f"{x['date']},{x['type']},{x['category']},{x['amount']}")
    else:
        print("No transactions available.")

def save_transactions(transactions):
    with open(file_name,"w") as f:
        json.dump(transactions,f,indent=4)


def add_transactions(transactions):
    date = datetime.now().strftime("%Y/%m/%d %H:%M")
    typed = input('Enter the type(Income/Expense): ')
    category = input("Enter the category of the transaction: ")
    amount = float(input("Enter the amount: "))
    transaction = dict(date = date, type = typed, category = category, amount = amount)
    transactions.append(transaction)
    save_transactions(transactions)

def update_transaction():
    pass
 



