balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance =", balance)

    elif choice == "2":
        amount = float(input("Enter amount: "))
        balance += amount
        print("New Balance =", balance)

    elif choice == "3":
        amount = float(input("Enter amount: "))

        if amount <= balance:
            balance -= amount
            print("New Balance =", balance)
        else:
            print("Insufficient Balance")

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")