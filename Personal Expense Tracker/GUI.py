import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import main 
import pandas as pd
import sys

class GUI:
    def __init__(self):
        self.cmd = main.Traker()
        self.window_setup()

    def window_setup(self):
        # Create the main self.root
        self.root = tk.Tk()
        self.root.title("Personal Expense Tracker")
        
        # Load existing expenses
        frame1 = tk.Frame(master=self.root, relief='flat', width=400, height=100)
        frame1.pack()

        label = tk.Label(master=frame1, text="Please load your csv expense file.")
        label.pack(fill=tk.Y, side=tk.LEFT)
        load_button = tk.Button(master=frame1, text="Open File", command=self.load_expenses)
        load_button.pack(fill=tk.Y, side=tk.LEFT)

        # Add expense
        frame2 = tk.Frame(master=self.root, relief='groove', width=400, height=100)
        frame2.pack()
        label = tk.Label(master=frame2, text="Add your exepense hereunder.")
        label.pack(fill=tk.Y, side=tk.LEFT)

        frame3 = tk.Frame(master=self.root, relief='ridge', width=400, height=400)
        frame3.pack()
        label = tk.Label(master=frame3, text="Date")
        label.grid(row=1,column=1)
        self.date_entry = ttk.Entry(master=frame3)
        self.date_entry.grid(row=1,column=2)

        label = tk.Label(master=frame3, text="Category")
        label.grid(row=2,column=1)
        self.category_entry = ttk.Entry(master=frame3)
        self.category_entry.grid(row=2,column=2)

        label = tk.Label(master=frame3, text="Description")
        label.grid(row=3,column=1)
        self.description_entry = ttk.Entry(master=frame3)
        self.description_entry.grid(row=3,column=2)

        label = tk.Label(master=frame3, text="Amount")
        label.grid(row=4,column=1)
        self.amount_entry = ttk.Entry(master=frame3)
        self.amount_entry.grid(row=4,column=2)

        
        add_expense_button = tk.Button(master=frame3, text="Add expense", command=self.add_expense)
        add_expense_button.grid(row=5,column=2)

        # View expenses 
        frame4 = tk.Frame(master=self.root, width=400, height=400)
        frame4.pack()
        label = tk.Label(master=frame4, text="View expenses")
        label.grid(row=1,column=1)
        view_expense_button = tk.Button(master=frame4, text="View expense", command=self.show_expenses)
        view_expense_button.grid(row=1,column=2)
        # Track budget 
        # Save expenses 
        # Exit

        # Run the application
        self.root.mainloop()

    def add_expense(self):
        output = self.cmd.input_expense(self.date_entry.get(), self.category_entry.get(), self.description_entry.get(), self.amount_entry.get())
        tk.messagebox.showinfo(title=output[0], message=output[1])
    
    def show_expenses(self):
        try:
            message, self.df = self.cmd.visualize_expenses()
            if message != "":
                tk.messagebox.showinfo("INFO", message)
        
            window = tk.Tk()
            window.title("Expenses")

            # Create Treeview widget (table)
            self.tree = ttk.Treeview(window)

            # Define columns (columns of the DataFrame)
            self.tree["columns"] = list(self.df.columns)

            # Format columns (show column names as headers)
            for col in self.df.columns:
                self.tree.heading(col, text=col,  command=lambda c=col: self.sort_by_column(c))

            # Sorting state: store the column and direction of sorting
            self.sort_column = None
            self.sort_reverse = False

            # Add data rows to the treeview
            self.insert_rows()

            # Pack the treeview widget
            self.tree.pack(expand=True, fill=tk.BOTH)
        except Exception as e:
            tk.messagebox.showwarning("WARNING", "No expenses to visualize")
            exc_type, exc_tb = sys.exc_info()
            print(exc_type, exc_tb.tb_lineno)
    
    def insert_rows(self):
        """Insert rows into the treeview widget."""
        # Clear any previous data in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert data from the DataFrame into the Treeview
        for _, row in self.df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def sort_by_column(self, col):
        # Check if the column clicked is the same as the last one, toggle sorting direction
        if self.sort_column == col:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_column = col
            self.sort_reverse = False
        
        # Sort the DataFrame by the column
        sorted_df = self.df.sort_values(by=col, ascending=not self.sort_reverse)
        
        # Re-insert rows in the new order
        self.df = sorted_df  # Update the DataFrame with sorted data
        self.insert_rows()    # Update the Treeview with sorted rows
    
    def run(self):
        # Run the Tkinter event loop
        self.root.mainloop()

    def ask_directory(self):   
        dir_name = filedialog.asksaveasfilename(filetypes=[("Csv files", "*.csv")])
        return dir_name
    
    def ask_filename(self):
        dir_name = filedialog.askopenfilename(filetypes=[("Csv files", "*.csv")])
        return dir_name

    def load_expenses(self):
        file_path = self.ask_filename()
        tk.messagebox.showinfo(title='Selected File', message=file_path)
        self.cmd.expenses_traker = pd.read_csv(file_path)

if __name__ == "__main__":
    # Create and run the GUI
    app = GUI()
    app.run()