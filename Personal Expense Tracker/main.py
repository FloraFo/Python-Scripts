import pandas as pd
import numpy as np
import datetime

class Traker:
    def __init__(self):
        self.expenses_traker = pd.DataFrame(columns=['date', 'category', 'amount', 'description'])
        self.budgets = {}

    def input_expense(self, date, category, description, amount):
        new_expense = {}
        msg_title= "Expense Added"
        msg = "Expense added."
        try:
            new_expense['date'] = datetime.date.fromisoformat(date)
        except:
            msg_title ="Date format error"
            msg = "Please insert the date in the following format 'YYYY-MM-DD'"
            return [msg_title, msg]
        new_expense['category'] = category
        new_expense['description'] = description
        
        try :
            new_expense['amount'] = float(str(amount).replace(",", "."))
        except Exception as e:
            msg_title = "Amount format error"
            msg = "Please insert the correct amount"
            return [msg_title, msg]
        
        self.store_expense(new_expense)
        return [msg_title, msg]

    def store_expense(self,new_expense):
        idx=len(self.expenses_traker)
        self.expenses_traker.loc[idx] = new_expense

    def visualize_expenses(self):
        message = "" 
        if np.where(pd.isnull(self.expenses_traker)):
            message = "Some entries are incomplete and have been hidden"
        self.expenses_traker.replace({'': np.nan, ' ': np.nan}, inplace=True)
        df = self.expenses_traker.dropna()
        return message, df

    def budget_setting(self, category, budget):
        self.budgets[category.lower()] = budget
        return self.track_budget(category)

    def track_budget(self, category):
        if category != "" :
            expenses_tracked = self.expenses_traker[self.expenses_traker["category"].str.lower() == category.lower()]
        else :
            expenses_tracked = self.expenses_traker

        if expenses_tracked["amount"].sum() >= self.budgets[category.lower()]:
            message = "WARNING: you have overachieved your budget on {} expenses.\nTotal spent amount: {}€".format(category.lower(), expenses_tracked["amount"].sum())
        else :
            message = "INFO: remaining budget on {} expenses : {}€".format(category.lower(), self.budgets[category.lower()] - expenses_tracked["amount"].sum())
        return message
    