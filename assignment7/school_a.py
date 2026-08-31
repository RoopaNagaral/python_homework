import sqlite3

# Connect to the database
with sqlite3.connect("db/school.db") as conn:
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        age INTEGER,
        major TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL UNIQUE,
        instructor_name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Enrollments (
        enrollment_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES Students (student_id),
        FOREIGN KEY (course_id) REFERENCES Courses (course_id)
    )
    """)

    """ # Insert sample data into tables
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Jasmine', 20, 'Computer Science')")
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Pratik', 22, 'History')") 
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Carlos', 19, 'Biology')") 
    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Math 101', 'Dr. Sanchez')")
    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('English 101', 'Ms. Jones')") 
    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Chemistry 101', 'Dr. Lee')") 

    conn.commit() 
    # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    print("Sample data inserted successfully.") """
    
    def add_student(cursor, name, age, major):
        try:
            cursor.execute("INSERT INTO Students (name, age, major) VALUES (?,?,?)", (name, age, major))
        except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")

    def add_course(cursor, name, instructor):
        try:
            cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES (?,?)", (name, instructor))
        except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")

with sqlite3.connect("db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
    cursor = conn.cursor()

    # Insert sample data into tables

    add_student(cursor, 'Jasmine', 20, 'Computer Science')  
    add_student(cursor, 'Pratik', 22, 'History')
    add_student(cursor, 'Carlos', 19, 'Biology')
    add_course(cursor, 'Math 101', 'Dr. Smith')
    add_course(cursor, 'English 101', 'Ms. Jones')
    add_course(cursor, 'Chemistry 101', 'Dr. Lee')

    conn.commit() 
    # If you don't commit the transaction, it is rolled back at the end of the with statement, and the data is discarded.
    print("Sample data inserted successfully.")
    
    cursor.execute("SELECT * FROM Students WHERE name = 'Jasmine'")
    result = cursor.fetchall()
    for row in result:
        print(row)
        
    def enroll_student(cursor, student, course):
        cursor.execute("SELECT * FROM Students WHERE name = ?", (student,)) # For a tuple with one element, you need to include the comma
        results = cursor.fetchall()
        if len(results) > 0:
            student_id = results[0][0]
        else:
            print(f"There was no student named {student}.")
            return
        cursor.execute("SELECT * FROM Courses WHERE course_name = ?", (course,))
        results = cursor.fetchall()
        if len(results) > 0:
            course_id = results[0][0]
        else:
            print(f"There was no course named {course}.")
            return
        cursor.execute("INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))

        ... # And at the bottom of your "with" block

        enroll_student(cursor, "Jasmine", "Math 101")
        enroll_student(cursor, "Jasmine", "Chemistry 101")
        enroll_student(cursor, "Pratik", "Math 101")
        enroll_student(cursor, "Pratik", "English 101")
        enroll_student(cursor, "Carlos", "English 101")
        conn.commit() # more writes, so we have to commit to make them final!
        
        