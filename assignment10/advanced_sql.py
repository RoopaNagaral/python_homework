import sqlite3
import os

# Note, you need to create a 'db' directory if it isn't already in your workspace
DB_PATH = "db/lesson.db"

# Start fresh so results are predictable when re-running this script
""" if os.path.exists(DB_PATH):
    os.remove(DB_PATH) """
conn = None
try:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    #Task 1: Complex JOINs with Aggregation
        
    query = """
        SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
        FROM orders AS o JOIN line_items AS li ON o.order_id = li.order_id
        JOIN products AS p ON p.product_id = li.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id LIMIT 5
        """
        
    cursor.execute(query)
    print("Total price of order: ")
    print(cursor.fetchall())
    
    #Task 2: Understanding Subqueries
    query2 = """
        SELECT c.customer_name, AVG(sub.total_price) AS average_total_price
        FROM customers AS c 
        LEFT JOIN (
            SELECT o.customer_id AS customer_id_b, SUM(p.price * li.quantity) AS total_price
                    FROM orders AS o JOIN line_items AS li ON o.order_id = li.order_id
                    JOIN products AS p ON p.product_id = li.product_id
                    GROUP BY o.order_id, o.customer_id
        ) sub ON c.customer_id = sub.customer_id_b
        GROUP BY customer_id
    """
    
    cursor.execute(query2)
    print("\nCustomer name and Avgerage total price of orders:")
    print(cursor.fetchall())    

    #Task 3.1: An Insert Transaction Based on Data
    
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
    customerid = cursor.fetchone()
    
    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
    empid = cursor.fetchone()
    
    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    productid = cursor.fetchall()
    
    cursor.execute("INSERT INTO orders(customer_id, employee_id, date) VALUES(?,?,?) RETURNING order_id", (int(customerid[0]), int(empid[0]), '2026-09-09'))
    orderid = cursor.fetchone()
    
    item_list = []
    for row in productid:
        product = int(row[0])
        quantity = 5
        cursor.execute("INSERT INTO line_items(order_id, product_id, quantity) VALUES(?,?,?)", (int(orderid[0]), product, 5))

        cursor.execute("""
                       SELECT li.line_item_id, p.product_name, li.quantity 
                       FROM line_items AS li JOIN products AS p ON li.product_id = p.product_id
                       WHERE li.order_id =? AND li.product_id =?
                       """,(int(orderid[0]), product,))
        item_list.append(cursor.fetchone())
        quantity += 1
        
        cursor.execute("DELETE FROM line_items WHERE order_id =? AND product_id =?",(int(orderid[0]), product,))
        cursor.execute("""
                              SELECT li.line_item_id, p.product_name, li.quantity 
                              FROM line_items AS li JOIN products AS p ON li.product_id = p.product_id
                              WHERE li.order_id =? AND li.product_id =?
                              """,(int(orderid[0]), product,))
        print("\n", cursor.fetchone())         
             
    print("\nOrder Details of customer 'Perez and Sons':")
    print(item_list) 
    
    cursor.execute("DELETE FROM orders WHERE order_id=?", (int(orderid[0]),))
    
    cursor.execute("SELECT * FROM orders WHERE order_id=?", (int(orderid[0]),))
    print("\n", cursor.fetchone())
    
    #Task 4: Aggregation with HAVING
    having_query = """
        SELECT e.employee_id, e.first_name, e.last_name, COUNT(e.employee_id)
        FROM employees AS e JOIN orders AS o ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(e.employee_id) > 5
    """
    cursor.execute(having_query)
    print("\nOrder of each employee:")
    print(cursor.fetchall())
    
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn is not None:
        conn.close()
        print("\nDatabase connection closed.") 