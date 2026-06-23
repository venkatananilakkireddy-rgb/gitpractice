students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks

    elif choice == "2":
        print("\nStudent Records:")
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == "3":
        name = input("Enter student name: ")
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")