# Personal Expense Traker

The **Personal Expense Tracker** is a simple application designed to help users manage their finances by tracking daily expenses, setting budgets, and categorizing spending. The app allows users to set monthly budgets for different categories, monitor their expenses, and view detailed reports. It also features file handling to save and load data, ensuring that users can easily keep track of their financial history. With an easy-to-use, menu-driven interface, this tool helps users stay on top of their spending and improve their financial management.


To develop this expense tracker application, I utilized the following libraries:
-	Pandas: For handling data structures, specifically for managing the expenses data and saving them to a CSV file.
-	NumPy: For performing numerical operations, such as calculating remaining budget or total expenses in each category.
-	Tkinter: For creating the graphical user interface (GUI) through which users can interact with the application.

# Code Structure

The code has been split into two separate .py files for better organization and readability:
*	**GUI Interactions** (GUI.py): This file handles all interactions with the graphical interface. It manages the display of the main window, input fields for adding expenses, and the presentation of the data.
*	**Expense Operations** (main.py): This file contains the logic for managing expenses, including operations such as adding, editing, and deleting expenses. It also handles file operations for loading and saving expense data.

# Additional Information

- Adding Expenses Without Pre-existing File: If the user does not load an existing file containing previously recorded expenses, they can still start adding expenses from scratch. In this case, the application will create a new file automatically upon saving the data.
- Optional Budget Limits by Category: Users have the flexibility to track their expenses either with a specific budget for each category or with a general budget for all expenses.
- Additional Notifications: I added helpful messages to enhance the user experience. For example, the application now displays the remaining budget or the amount already spent in each category, allowing users to easily track their financial status.

# Conclusion
This expense tracker application is designed to be user-friendly and flexible. The combination of Tkinter for the interface, Pandas for data management, and NumPy for calculations makes the application efficient and easy to use. The modifications I made to the original project allow for greater user flexibility, whether they are starting fresh or working with existing data, and the added notifications provide useful insights into their spending.

