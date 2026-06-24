while True:
    print("\n1. Save Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        website = input("Website: ")
        password = input("Password: ")

        with open("vault.txt", "a") as file:
            file.write(f"{website} : {password}\n")

        print("Saved Successfully")

    elif choice == "2":
        try:
            with open("vault.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No passwords saved")

    elif choice == "3":
        print("Goodbye!")
        break