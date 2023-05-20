### Expense tracker with CSV to store values


import csv

expenses = []
password = 1234
filename = "expenses.csv"

while True:
    print()
    print("===========Expense Tracker===========")
    print("1. Open User Options")
    print("2. Open Admin Settings")
    print("3. Memory options")
    print("4. Quit")
    print("=====================================")
    
    choice = input("Enter your choice: ")

##########################################################################

    if choice == "1":
        while True: 
            print()
            print("=============User Options============")
            print("1. Add Expense")
            print("2. View Total Expenses")
            print("3. View Expenses by Category")
            print("4. Return to main menu")
            print("=====================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter the username: ")
                category = input("Enter the expense category: ")
                amount = float(input("Enter the expense amount: "))
                expenses.append((username, (category, amount)))
                print("Expense added successfully!")
                print("=====================================")
                print()

            elif choice == "2":
                sum = 0
                username = input("Enter the username: ")
                for i in expenses:
                    if i[0] == username:
                        sum += i[1][1]
                print ("Total Expenses: ", sum)
                print("=====================================")
                print()

            elif choice == "3":
                print("Expenses by Category:")
                username = input("Enter the username: ")
                for i in expenses:
                    if i[0] == username:
                        print(i[1][0], ":", i[1][1])
                print("=====================================")
                print()

            elif choice == "4":
                print("=====================================")
                break

##########################################################################

    elif choice == "2":
        while True:
            print()
            print("============Admin Settings===========")
            print("1. Print all the Usernames")
            print("2. Change password")
            print("3. Return to main menu")
            print("=====================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("Expenses by Username:")
                admin= int(input("Enter the Admin Password: "))
                if admin == password:
                    for i in expenses:
                        print(i[0])
                        print(i[1][0], ":", i[1][1])
                        print()
                    print("=====================================")
                    print()
                else:
                    print("Access Denied")
                    print("=====================================")
                    print()
                        

            elif choice == "2":
                print("Change Password:")
                admin= int(input("Enter the Current Admin Password: "))
                if admin == password:
                    password = int(input("Enter the New Admin Password: "))
                    print("Password Changed successfully")
                    print("NOTE: Running the program again will") 
                    print("reset the password to default")
                else:
                    print("Access Denied")
                print("=====================================")
                print()
            
            elif choice == "3":
                print("=====================================")
                break

##########################################################################
    elif choice == "3":
        while True:
            print()
            print("============Memory Options===========")
            print("1. Save Data")
            print("2. Load Data")
            print("3. Return to main menu")
            print("=====================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                with open(filename, "w", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(expenses)

            elif choice == "2":
                with open(filename, "r") as csvfile:
                    reader = csv.reader(csvfile)
                    expenses.extend(list(reader))

            elif choice == "3":
                print("=====================================")
                break

##########################################################################        
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        print("=====================================")
        break

    else:
        print("Invalid choice. Please try again.")
        print("=====================================")
        print()
