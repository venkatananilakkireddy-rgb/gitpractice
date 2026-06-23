balance = 1000

def check_balance():
    print("Balance =", balance)

def deposit():
    global balance
    amount = float(input("Enter amount: "))
    balance += amount
    print("Deposited Successfully")

def withdraw():
    global balance
    amount = float(input("Enter amount: "))

    if amount <= balance:
        balance -= amount
        print("Withdraw Successful")
    else:
        print("Insufficient Balance")

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")