while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        expense = input("Enter expense: ")

        with open("expenses.txt", "a") as file:
            file.write(expense + "\n")

        print("Expense Saved")

    elif choice == "2":
        try:
            with open("expenses.txt", "r") as file:
                print("\nExpenses:")
                print(file.read())
        except FileNotFoundError:
            print("No expenses found")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")