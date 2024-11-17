import pandas as pd
import numpy as np
import datetime
import GUI

class Traker:
    def __init__(self):
        #self.gui = GUI.GUI()
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
        print(self.expenses_traker)
        self.expenses_traker.replace({'': np.nan, ' ': np.nan}, inplace=True)
        df = self.expenses_traker.dropna()
        print(df)
        return message, df

    def budget_setting(self, category="all"):
        try :
            budget = float(str(input("Please indicate the budget for {} category: ".format(category.lower()))).replace(",", "."))
        except Exception as e:
            print("Please insert the correct amount")
            raise ValueError("Incorrect amount format")
        self.budgets[category.lower()] = budget

    def track_budget(self, category="all"):
        if category != "all" :
            expenses_tracked = self.expenses_traker[self.expenses_traker["category"].str.lower() == category.lower()]
        else :
            expenses_tracked = self.expenses_traker

        if expenses_tracked["amount"].sum() >= self.budgets[category.lower()]:
            print("WARNING: you have overachieved your budget on {} expenses.\nTotal spent amount: {}€".format(category.lower(), expenses_tracked["amount"].sum()))
        else :
            print("INFO: remaining budget on {} expenses : {}€".format(category.lower(), self.budgets[category.lower()] - expenses_tracked["amount"].sum()))

    def save_expenses(self):
        dir = self.gui.ask_directory()
        self.expenses_traker.to_csv(dir+".csv", index=False)
        print("File saved at location: ", dir)

    def load_expenses(self):
        file_path = self.gui.ask_filename()
        expenses_traker = pd.read_csv(file_path)
        return expenses_traker


#expenses_traker = load_expenses()
#input_expense()
#budget_setting("Food")
#visualize_expenses()
#track_budget("food")
#save_expenses()
