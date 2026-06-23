expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)

    elif choice == "2":
        print("Expenses:")
        for expense in expenses:
            print(expense)

    elif choice == "3":
        print("Total Expense =", sum(expenses))

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")