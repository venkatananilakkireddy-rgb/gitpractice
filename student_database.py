import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        cursor.execute(
            "INSERT INTO students (name, marks) VALUES (?, ?)",
            (name, marks)
        )

        conn.commit()
        print("Student Added")

    elif choice == "2":
        cursor.execute("SELECT * FROM students")

        for row in cursor.fetchall():
            print(row)

    elif choice == "3":
        break

conn.close()