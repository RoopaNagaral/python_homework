import csv
import traceback

# Task 3
with open("csv/employees.csv","r") as file:
    reader = csv.reader(file)
    fields = next(reader)
    emp_list = [row for row in reader]
    emp_name_list = []
    for row in emp_list:
        emp_name_list.append(row[1] + ' ' + row[2])
    
    print("Output of Task 3:")
    print(emp_name_list)
    
    emp_filtered_list = list(filter(lambda n: "e" in n, emp_name_list))
    print("\nList of names with letter e:", emp_filtered_list)