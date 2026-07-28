import pandas as pd
import json
import os

# Task 1: Creating and Manipulating DataFrames
# 1.1: creating DataFrame from dictionary
task1_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }

task1_data_frame = pd.DataFrame(task1_data)
print("DataFrame: \n",task1_data_frame)

# 1.2: copying main dataframe to new dataframe and adding salary column to new dataframe
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("\n Salary column: \n", task1_with_salary)

# 1.3: copying recent dataframe to new dataframe and incrementing age column by 1
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print("\n Age Increment: \n", task1_older)

# 1.4: save the dataframe to csv file
task1_older.to_csv("./employees.csv", index=False)

# Task 2: Loading Data from CSV and JSON
# 2.1: read data from csv file
task2_employees = pd.read_csv("./employees.csv")
print("\n Data from csv file: \n", task2_employees)

# 2.2: create JSON file and add data
new_emp = {
    'Name': ['Eve', 'Frank'],
    'Age': [28, 40],
    'City': ['Miami', 'Seattle'],
    'Salary': [60000, 95000]  
}
with open("additional_employees.json", "w") as file:
     json.dump(new_emp, file)

json_employees = pd.read_json("./additional_employees.json")
print("\nJson file data: \n", json_employees)

# 2.3: combine data from json and csv file
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\n Combined data: \n", more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
# 3.1: Read first three rows using head() method
first_three = more_employees.head(3)
print("\n First three rows of employees data: \n", first_three)

# 3.2: Read last two rows using tail() method
last_two = more_employees.tail(2)
print("\n Last two row of employees data: \n", last_two)

# 3.3: get the shape of dataframe
employee_shape = more_employees.shape
print("\n Shape of the dataframe: \n", employee_shape)

# 3.4: get the summary of the DataFrame using the info()
print("\n Summary of datatframe: ")
more_employees.info()

# Task 4: Data Cleaning
# 4.1: create dataframe from dirty_data.csv file
path = os.path.join(os.getcwd(), 'dirty_data.csv')
dirty_data = pd.read_csv(path)
print("\n Dirty data: \n", dirty_data)

clean_data = dirty_data.copy()

# 4.2: remove duplicate rows
clean_data = clean_data.drop_duplicates()
print("\n No duplicates: \n", clean_data)

# 4.3: Convert Age to numeric and handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print("\n Numeric Age: \n", clean_data)

# 4.4: Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data["Salary"] = clean_data["Salary"].replace("unknown", pd.NA)
clean_data["Salary"] =clean_data["Salary"].replace("n/a", pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print("\n Numeric Age: \n", clean_data)

# 4.5: Fill missing numeric values (use fillna).  Fill Age with the mean and Salary with the median
mean_age = clean_data["Age"].mean()
clean_data["Age"] = clean_data["Age"].fillna(mean_age)

median_salary = clean_data["Salary"].median()
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)
print("\n Mean Age and Median Salary: \n", clean_data)

# 4.6: Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
print("\n Converted Hire Date: \n", clean_data)

# 4.7: Strip extra whitespace and standardize Name and Department as uppercase
clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Name"] = clean_data["Name"].str.upper()

clean_data["Department"] = clean_data["Department"].str.strip()
clean_data["Department"] = clean_data["Department"].str.upper()
print("\n Uppercase Name & Department: \n", clean_data)
