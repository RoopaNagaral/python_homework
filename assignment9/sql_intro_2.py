import pandas as pd
import sqlite3

#Task 5: Read Data into a DataFrame
with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT line_items.line_item_id, line_items.quantity, products.product_id, products.product_name, products.price 
                        FROM line_items JOIN products ON line_items.product_id = products.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print("\nLesson database to dataframe:")
    print(df.head())
    
    #add total column to df
    df['total'] = df['quantity'] * df['price']
    print("\nTotal of quantity into price")
    print(df.head())
    
    #group by product_id and different aggrigation
    df = df.groupby('product_id').agg({
        'line_item_id' : 'count',
        'total' : 'sum',
        'product_name': 'first'})
    print("\nAggrigation:")
    print(df.head())
    
    #sort by product name
    df = df.sort_values(by="product_name", ascending=True)
    print("\nSorted by product name:")
    print(df.head())
    
    #writing dataframe to csv file
    df.to_csv("order_summary.csv", index=False)