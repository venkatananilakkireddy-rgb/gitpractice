passwords = {}

while True:
    print("\n1. Add Password")
    print("2. View Accounts")
    print("3. Search Password")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        website = input("Enter website: ")
        password = input("Enter password: ")
        passwords[website] = password

    elif choice == "2":
        print("\nSaved Accounts:")
        for website in passwords:
            print(website)

    elif choice == "3":
        website = input("Enter website: ")

        if website in passwords:
            print("Password:", passwords[website])
        else:
            print("Website not found")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")