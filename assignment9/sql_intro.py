import sqlite3

# Task 1: Create a New SQLite Database
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        print("Database created and connected successfully.")
        cursor = conn.cursor()
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    conn.commit()
    
    #Task 2: Define Database Structure
    
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        cursor = conn.cursor()
        # create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            publisher_name TEXT NOT NULL UNIQUE
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazines_id INTEGER PRIMARY KEY,
            publisher_id INTEGER,
            magazine_name TEXT NOT NULL UNIQUE,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            subscriber_name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)
                
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            magazines_id INTEGER,
            subscriber_id INTEGER,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (magazines_id) REFERENCES magazines (magazines_id),
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id)
        )
        """)
        
        print("Tables created successfully.")
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:       
    conn.commit()
       
    #Task 3: Populate Tables with Data
    
    def add_publishers(cursor, name):
        try:
            cursor.execute("INSERT INTO publishers (publisher_name) VALUES (?)", (name,))
        except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")
            
    def add_subscribers(cursor, name, address):
        try:
            cursor.execute("SELECT * FROM subscribers WHERE subscriber_name = ? AND address = ?", (name, address))
            results = cursor.fetchall()
            if len(results) <= 0:
                cursor.execute("INSERT INTO subscribers (subscriber_name, address) VALUES (?,?)", (name, address))
            else:
                print(f"The {name} and {address} of subcriber is alredy exists.")
                return
                
        except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")
    
    def add_magazines(cursor, publisher, name):
            try:
                cursor.execute("SELECT * FROM publishers WHERE publisher_name = ?", (publisher,)) # For a tuple with one element, you need to include the comma
                results = cursor.fetchall()
                if len(results) > 0:
                    publisher_id = results[0][0]
                else:
                    print(f"There was no publisher named {publisher}.")
                    return
                cursor.execute("INSERT INTO magazines (publisher_id, magazine_name) VALUES (?,?)", (publisher_id, name))
            except sqlite3.IntegrityError:
                print(f"{name} is already in the database.")
                
    def add_subscriptions(cursor, magazines, subscriber, expirationDate):
        try:
            cursor.execute("SELECT * FROM magazines WHERE magazine_name = ?", (magazines,)) # For a tuple with one element, you need to include the comma
            results = cursor.fetchall()
            if len(results) > 0:
                magazines_id = results[0][0]
            else:
                print(f"There was no magazine named {magazines}.")
                return
            cursor.execute("SELECT * FROM subscribers WHERE subscriber_name = ?", (subscriber,)) # For a tuple with one element, you need to include the comma
            results = cursor.fetchall()
            if len(results) > 0:
                subscriber_id = results[0][0]
            else:
                print(f"There was no subcriber named {subscriber}.")
                return
            cursor.execute("INSERT INTO subscriptions (magazines_id, subscriber_id, expiration_date) VALUES (?,?,?)", (magazines_id, subscriber_id, expirationDate))
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
        cursor = conn.cursor()             
    # Insert sample data into tables
    
    add_publishers(cursor, 'The N2 Company')  
    add_publishers(cursor, 'Home Upgrades, Inc.')
    add_publishers(cursor, 'Style Creative Media LLC')
    
    add_subscribers(cursor, 'Dr. Smith', '9151 Currency St, Irving, TX 75063')
    add_subscribers(cursor, 'Ms. Jones', '3900 W Plano Pkwy, Plano, TX 75075')
    #add_subscribers(cursor, 'Dr. Smith', '9151 Currency St, Irving, TX 75063')
    add_subscribers(cursor, 'Dr. Lee', '15443 Knoll Trail Dr, Dallas, TX 75248')
    
    add_magazines(cursor,'The N2 Company','Greet')
    add_magazines(cursor, 'Home Upgrades, Inc.','Horticulture')
    add_magazines(cursor, 'Style Creative Media LLC','Allrecipes')
    
    add_subscriptions(cursor, 'Greet','Dr. Smith','09/20/2026')
    add_subscriptions(cursor, 'Horticulture', 'Ms. Jones','09/25/2026')
    add_subscriptions(cursor, 'Allrecipes', 'Dr. Lee', '09/30/2026')
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    conn.commit()
 
#Task 4: Write SQL Queries
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        cursor = conn.cursor()
    # Retrieve all information from the subscribers table
    try:
        cursor.execute("SELECT * FROM subscribers")
        result = cursor.fetchall()
        print("\n Information of Subscibers: ")
        for row in result:
            print(row)
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    
    #retrieve all magazines sorted by name  
    try:
        cursor.execute("SELECT * FROM magazines ORDER BY magazine_name")
        result = cursor.fetchall()
        print("\n Information of Magazines: ")
        for row in result:
            print(row)
    except sqlite3.Error as e:
        print(f"Database error: {e}")        
        
    #find magazines for a particular publisher
    try:
        cursor.execute("SELECT m.magazine_name, p.publisher_name FROM magazines AS m JOIN publishers AS p ON m.publisher_id = p.publisher_id WHERE p.publisher_name = 'The N2 Company'")
        result = cursor.fetchall()
        print("\n Information of Magazines: ")
        for row in result:
            print(row)
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    conn.commit()
        

