import csv
import traceback

# Task 3
with open("csv/employees.csv","r") as file:
    reader = csv.reader(file)
    employees = list(reader)

    names = [row[1] + " " + row[2] for row in employees[1:]]
    print(names)

    names_with_e = [name for name in names if "e" in name.lower()]
    print("\n", names_with_e)

    # --- Task Completed ---