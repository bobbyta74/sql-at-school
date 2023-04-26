import csv
import sqlite3

connection = sqlite3.connect("starbucks.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS drinks;")

cursor.execute("""
    CREATE TABLE drinks(
        category text,
        beverage text,
        customization text,
        size text,
        calories integer);
    """)

with open("starbucks.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    headings = next(csv_reader)
    for row in csv_reader:
        category, beverage, customization, size, calories = row
        
        cursor.execute("""
            INSERT INTO drinks VALUES(?,?,?,?,?)
        """, [ category, beverage, customization, size, calories ])
        
connection.commit()
cursor.close()    
connection.close()



