import sqlite3
import os

def query(dbname):
    connection = sqlite3.connect(dbname)

    while True:
        sql = input("SQL: ")
        if sql == "": break
        cursor = connection.cursor()
        try:
            results = cursor.execute(sql)
            for row in results: print(list(row))
        except sqlite3.Error as e:
            print(e)
        cursor.close()
        
    connection.close()

dbname = input("Enter the database name:")
if not dbname.endswith(".db"):
    dbname += ".db"
if os.path.exists(dbname):
    query(dbname)
else:
    print(f"Database not found: {dbname}")
