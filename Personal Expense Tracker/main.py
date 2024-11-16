import pandas as pd
import numpy as np
import datetime


expenses_traker = pd.DataFrame(columns=['date', 'category', 'amount', 'description'])

def input_expense():
    new_expense = {}
    try:
        new_expense['date'] = datetime.date.fromisoformat(input("Please indicate the date of you expense in format 'YYYY-MM-DD'"))
    except:
        print("Please insert the date in the following format 'YYYY-MM-DD': ")
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
 
    new_expense['category'] = input("Please indicate the category of the expense: ")
    new_expense['description'] = input("Please provide a short description of the expense: ")
    
    try :
        new_expense['amount'] = float(str(input("Please indicate the amount of your expense: ")).replace(",", "."))
    except Exception as e:
        print("Please insert the correct amount")
        raise ValueError("Incorrect amount format")
    return new_expense

def store_expense(new_expense):
    idx=len(expenses_traker) -1
    expenses_traker.loc[idx] = new_expense
    print(expenses_traker)
    return expenses_traker

def visualize_expenses():
    if np.where(pd.isnull(expenses_traker)):
        print("Some entries are incomplete and have been hidden")
    print(expenses_traker.dropna(axis=0).to_string(index=False))

store_expense(input_expense())