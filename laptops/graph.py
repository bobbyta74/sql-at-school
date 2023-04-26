import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

connection = sqlite3.connect("laptops.db")

while True:
    sql = "SELECT Ram, Price FROM laptops WHERE Company='Apple'"
    if sql == "":
        break
    cursor = connection.cursor()
    try:
        results = pd.read_sql_query(sql, connection)
        df = pd.DataFrame(results)
        plt.scatter(df['Ram'], df['Price'])
        plt.xlabel('RAM (GB)')
        plt.ylabel('Price ($)')
        plt.title('Apple Laptop Price vs RAM')
        plt.show()
    except sqlite3.Error as e:
        print(e)
    cursor.close()