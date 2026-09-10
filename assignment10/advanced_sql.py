import sqlite3
import os

# Note, you need to create a 'db' directory if it isn't already in your workspace
DB_PATH = "db/lesson.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
    
conn.execute("PRAGMA foreign_keys = 1;")

try:
    
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
        SELECT customer_name,
                   AVG(total_price) AS average_total_price
            FROM customers
            LEFT JOIN (
                SELECT customer_id AS customer_id_b,
                       SUM(products.price * line_items.quantity) AS total_price
                FROM orders
                JOIN line_items
                    ON orders.order_id = line_items.order_id
                JOIN products
                    ON line_items.product_id = products.product_id
                GROUP BY orders.order_id
            ) AS order_totals
                ON customer_id = customer_id_b
            GROUP BY customer_id
    """
    cursor.execute(query2)
    print("\nAverage total price of the customer order:")
    for customer_name, average_total_price in cursor.fetchall():
        if average_total_price is None:
            print(f"{customer_name}: No order total available")
        else:
            print(f"customer_name :{customer_name}, average_total_price:${average_total_price:.2f}")   

    #Task 3.1: An Insert Transaction Based on Data
    with conn:
        conn.execute("BEGIN")
        # 1. Get customer_id
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
        customerid = cursor.fetchone()[0]
        
        # 2. Get employee_id
        cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
        empid = cursor.fetchone()[0]
        
        # 3. Get 5 least expensive product_ids
        cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
        products = cursor.fetchall()
        
        # 4. Insert order and capture order_id
        cursor.execute("""
                    INSERT INTO orders (customer_id, employee_id, date)
                    VALUES (?, ?, date('now'))
                    RETURNING order_id
            """, (customerid, empid))
        order_id = cursor.fetchone()[0]

        # 5. Insert line items
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
            GROUP BY employees.employee_id
            HAVING COUNT(orders.order_id) > 5
    """
    cursor.execute(having_query)
    print("\nEmployee order details:")
    for employee_id, first_name, last_name, order_count in cursor.fetchall():
        print(
            f"employee_id: {employee_id}, "
            f"first_name: {first_name}, last_name: {last_name}, order_count: {order_count}"
        )
    
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Transaction failed:", e)
finally:
    conn.close()