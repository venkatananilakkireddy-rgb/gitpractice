books = []

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)

    elif choice == "2":
        print("\nBooks:")
        for book in books:
            print("-", book)

    elif choice == "3":
        book = input("Enter book name: ")

        if book in books:
            print("Book Found")
        else:
            print("Book Not Found")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")