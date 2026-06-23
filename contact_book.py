contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone

    elif choice == "2":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")