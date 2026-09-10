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
    
    cursor.execute("PRAGMA foreign_keys = 1;")

    #Task 1: Complex JOINs with Aggregation
        
    query = """
        SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
        FROM orders AS o JOIN line_items AS li ON o.order_id = li.order_id
        JOIN products AS p ON p.product_id = li.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id 
        LIMIT 5
        """
    cursor.execute(query)
    for order_id, total_price in cursor.fetchall():
        print(f"Order ID: {order_id}, Total price: ${total_price:.2f}")   
    
    #Task 2: Understanding Subqueries
    query2 = """
        SELECT customers.customer_name,
                   AVG(order_totals.total_price) AS average_total_price
            FROM customers
            LEFT JOIN (
                SELECT orders.customer_id AS customer_id_b,
                       SUM(products.price * line_items.quantity) AS total_price
                FROM orders
                JOIN line_items
                    ON orders.order_id = line_items.order_id
                JOIN products
                    ON line_items.product_id = products.product_id
                GROUP BY orders.order_id, orders.customer_id
            ) AS order_totals
                ON customers.customer_id = order_totals.customer_id_b
            GROUP BY customers.customer_id, customers.customer_name
            ORDER BY customers.customer_id;
    """
    cursor.execute(query2)
    print("\nAverage total price of the customer order:")
    for customer_name, average_total_price in cursor.fetchall():
        if average_total_price is None:
            print(f"{customer_name}: No order total available")
        else:
            print(f"Customer Name:{customer_name}, Average Total Price:${average_total_price:.2f}")   

    #Task 3.1: An Insert Transaction Based on Data
    
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
    customerid = cursor.fetchone()
    
    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
    empid = cursor.fetchone()
    
    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    products = cursor.fetchall()
    
    cursor.execute("""
                INSERT INTO orders (customer_id, employee_id, date)
                VALUES (?, ?, date('now'))
                RETURNING order_id
        """, (int(customerid[0]), int(empid[0])))
    order_id = cursor.fetchall()[0][0]

    cursor.executemany("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?)
            """, [(order_id, product_id, 10)
        for (product_id,) in products])

    print(f"\nTask 3: Line items for new order {order_id}")

    cursor.execute("""
            SELECT line_items.line_item_id,
                   line_items.quantity,
                   products.product_name
            FROM line_items
            JOIN products
                ON line_items.product_id = products.product_id
            WHERE line_items.order_id = ?
            ORDER BY line_items.line_item_id
        """, (order_id,))
    print("\nProduct details:")
    for line_item_id, quantity, product_name in cursor.fetchall():
        print(
            f"Line item ID: {line_item_id}, "
            f"Quantity: {quantity}, Product: {product_name}"
        )
          
    #Task 4: Aggregation with HAVING
    having_query = """
        SELECT employees.employee_id,
                   employees.first_name,
                   employees.last_name,
                   COUNT(orders.order_id) AS order_count
            FROM employees
            JOIN orders
                ON employees.employee_id = orders.employee_id
            GROUP BY employees.employee_id,
                     employees.first_name,
                     employees.last_name
            HAVING COUNT(orders.order_id) > 5
            ORDER BY employees.employee_id;
    """
    cursor.execute(having_query)
    print("\nEmployee order details:")
    for employee_id, first_name, last_name, order_count in cursor.fetchall():
        print(
            f"Employee ID: {employee_id}, "
            f"Name: {first_name} {last_name}, Orders: {order_count}"
        )
    
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn is not None:
        conn.close()
        print("\nDatabase connection closed.") 