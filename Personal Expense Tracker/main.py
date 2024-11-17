import pandas as pd
import numpy as np
import datetime
import tkinter as tk
from tkinter import filedialog

expenses_traker = pd.DataFrame(columns=['date', 'category', 'amount', 'description'])
budgets = {}

def input_expense():
    new_expense = {}
    try:
        new_expense['date'] = datetime.date.fromisoformat(input("Please indicate the date of you expense in format 'YYYY-MM-DD': "))
    except:
        print("Please insert the date in the following format 'YYYY-MM-DD'")
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
 
    new_expense['category'] = input("Please indicate the category of the expense: ").lower()
    new_expense['description'] = input("Please provide a short description of the expense: ")
    
    try :
        new_expense['amount'] = float(str(input("Please indicate the amount of your expense: ")).replace(",", "."))
    except Exception as e:
        print("Please insert the correct amount")
        raise ValueError("Incorrect amount format")
    store_expense(new_expense)
    return new_expense

def store_expense(new_expense):
    idx=len(expenses_traker) -1
    expenses_traker.loc[idx] = new_expense
    return expenses_traker

def visualize_expenses():
    if np.where(pd.isnull(expenses_traker)):
        print("Some entries are incomplete and have been hidden")
    print(expenses_traker.dropna(axis=0).to_string(index=False))

def budget_setting(category="all"):
    try :
        budget = float(str(input("Please indicate the budget for {} category: ".format(category.lower()))).replace(",", "."))
    except Exception as e:
        print("Please insert the correct amount")
        raise ValueError("Incorrect amount format")
    budgets[category.lower()] = budget

def track_budget(category="all"):
    if category != "all" :
        expenses_tracked = expenses_traker[expenses_traker["category"].str.lower() == category.lower()]
    else :
        expenses_tracked = expenses_traker

    if expenses_tracked["amount"].sum() >= budgets[category.lower()]:
        print("WARNING: you have overachieved your budget on {} expenses.\nTotal spent amount: {}€".format(category.lower(), expenses_tracked["amount"].sum()))
    else :
        print("INFO: remaining budget on {} expenses : {}€".format(category.lower(), budgets[category.lower()] - expenses_tracked["amount"].sum()))

def ask_directory():
    root = tk.Tk()
    root.withdraw()
    dir_name = filedialog.asksaveasfilename(filetypes=[("Csv files", "*.csv")])
    return dir_name

def save_expenses():
    dir = ask_directory()
    expenses_traker.to_csv(dir+".csv", index=False)
    print("File saved at location: ", dir)

def ask_filename():
    root = tk.Tk()
    root.withdraw()
    dir_name = filedialog.askopenfilename(filetypes=[("Csv files", "*.csv")])
    return dir_name

def load_expenses():
    file_path = ask_filename()
    expenses_traker = pd.read_csv(file_path)
    return expenses_traker


expenses_traker = load_expenses()
input_expense()
budget_setting("Food")
visualize_expenses()
track_budget("food")
save_expenses()