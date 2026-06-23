import csv

total = 0

with open("marks.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        total += int(row[1])

print("Total Marks =", total)