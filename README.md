# Expense Tracker with CSV Data Storage

This is a simple Expense Tracker program written in Python. The program allows users to add and track their expenses, view total expenses, view expenses by category, and provides admin settings to manage user data. The data is stored and retrieved using a CSV file, enabling users to save and load their expense records even after closing the program.

## How to Use

1. When you run the program, you will be presented with a menu that offers several options:

===========Expense Tracker===========
1. Open User Options
2. Open Admin Settings
3. Memory Options
4. Quit
=====================================



2. Choose an option by entering the corresponding number.

### User Options

1. **Add Expense:** Allows the user to add a new expense. You need to enter your username, the expense category, and the expense amount.

2. **View Total Expenses:** Displays the total expenses of a specific user. Enter your username to view the total expenses.

3. **View Expenses by Category:** Shows expenses of a specific user categorized by expense category. Enter your username to view the expenses.

### Admin Settings

1. **Print all the Usernames:** Requires the admin password to access. Once authenticated, it displays the usernames and their respective expenses.

2. **Change Password:** Requires the current admin password for authentication. If the current password is correct, you can set a new admin password. Note that the password will reset to the default when the program is run again.

### Memory Options

1. **Save Data:** Saves all the expenses in a CSV file named "expenses.csv".

2. **Load Data:** Loads previously saved expenses from the "expenses.csv" file.

### Important Note

- The default admin password is set to "1234". The admin password can be changed using the "Change Password" option.

- When you run the program again, the password will be reset to the default value, and any saved data will be loaded.

### Data Storage

All the user expenses are stored in a CSV file named "expenses.csv" in the same directory as the Python script. The data is written and read from this file using the CSV module, allowing for easy storage and retrieval of expense records.

### How to Run

1. Save the provided Python script in a file, for example, "expense_tracker.py".

2. Make sure you have Python installed on your system.

3. Open a terminal or command prompt in the same directory as the Python script.

4. Run the script using the following command:
python expense_tracker.py


5. Follow the on-screen instructions to use the Expense Tracker.

### Dependencies

This program uses the built-in `csv` module in Python, which does not require any additional installation.

### Limitations and Future Improvements

- The program currently stores all data in memory while the program is running. For larger datasets, it may be more efficient to use a database or other persistent storage methods.

- Adding authentication for individual users could enhance security and privacy.

- The program could be improved with features like expense modification, date tracking, and graphical analysis of expenses.

- Error handling and input validation could be added to make the program more robust.

- It's essential to keep the "expenses.csv" file secure and avoid sharing it publicly to protect sensitive expense data.

Remember that this is a simple expense tracker program meant for educational purposes and may not be suitable for real-world financial management.
