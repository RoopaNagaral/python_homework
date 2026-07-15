import os
import csv
import traceback
from itertools import zip_longest
import custom_module
from datetime import datetime


# Task 2
def read_employees():
    try:
        with open("../csv/employees.csv","r") as file:
            reader = csv.reader(file)
            fields = next(reader)
            rows = [list(row) for row in reader]
                
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    else:
        return {"fields": fields, "rows": rows}
    
employees = read_employees()
print("\n Output of Task 2:")
print(employees)

# Task 3
def column_index(key):
   return employees["fields"].index(key)

employee_id_column = column_index("employee_id")
print("\n Output of Task 3:")
print(employee_id_column)

# Task 4
def first_name(row_index):
    column_num = column_index("first_name")
    fst_name = employees["rows"][row_index][column_num]
    return fst_name
    
print("\n Output of Task 4:")
print("First Name:", first_name(4))

# Task 5
def employee_find(employee_id):
    def employee_match(row):
            return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches
print("\n Output of Task 5:")
print(employee_find(2))

# Task 6
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

print("\n Output of Task 6:")
print(employee_find_2(5))

# Task 7
def sort_by_last_name():
    last_name_index = column_index("last_name")
    #emp_list = list(employees["rows"])
    #sorted_list = sorted(emp_list, key= lambda row : row[column_id])
    employees["rows"].sort(key=lambda row : row[last_name_index])
    
    return employees["rows"]

print("\n Output of Task 7:")
print(sort_by_last_name())

# Task 8
def employee_dict(row):
    emp_dict = {}
    
    for index,field in enumerate(employees["fields"]):
        if field == "employee_id":
            continue
        emp_dict[field] = row[index]
    return emp_dict 

print("\n Output of Task 8:")
print(employee_dict(employees["rows"][1]))

# Task 9
def all_employees_dict():
    emp_dict = {}
    
    for row in employees["rows"]:
        emp_id = row[0]
        emp_dict[emp_id] = employee_dict(row)
    return emp_dict

print("\n Output of Task 9:")
print(all_employees_dict())

# Task 10
def get_this_value():
   return os.getenv("THISVALUE")

print("\n Output of Task 10:")
print(get_this_value())

# Task 11
def set_that_secret(secret):
    custom_module.set_secret(secret)

set_that_secret("Code")
print("\n Output of Task 11:")
print(custom_module.secret)

# Task 12
def read_minutes_file(path):
    try:
        with open(path, newline="") as file:
            reader = csv.reader(file)
            fields = next(reader)
            rows = [tuple(row) for row in reader]
                
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    else:
        return {"fields": fields, "rows":rows}
    
def read_minutes():
    v1 = read_minutes_file("../csv/minutes1.csv")
    v2 = read_minutes_file("../csv/minutes2.csv")
    return v1, v2

minutes1, minutes2 = read_minutes()
print("\n Output of Task 12:")
print(minutes1, minutes2)

# Task 13
def create_minutes_set():
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])

    minutes_combined = minutes1_set.union(minutes2_set)
    return minutes_combined

minutes_set = create_minutes_set()
print("\n Output of Task 13:")   
print(minutes_set)

# Task 14
def create_minutes_list():
    #minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
    minutes_list = list(minutes_set)
    converted_list = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list)
    return list(converted_list)

minutes_list  = create_minutes_list()
print("\n Output of Task 14:")   
print(minutes_list)

# Task 15
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x : x[1])
    converted = [(name, dt.strftime("%B %d, %Y")) for name, dt in sorted_list]
    
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        
        writer.writerow(minutes1["fields"])
        
        for row in converted:
            writer.writerow(row)
    return converted

minutes_sorted  = write_sorted_list()
print("\n Output of Task 14:")   
print(minutes_sorted)
        