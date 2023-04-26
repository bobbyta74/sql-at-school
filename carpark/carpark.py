import sqlite3
from datetime import datetime

connection = sqlite3.connect("cars.db")
cursor = connection.cursor()

try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars(
            plate text PRIMARY KEY,
            entrytime real
        );""")
except sqlite3.Error as e:
    print(e)
    
def myprogram():
    while True:
        try:
            plate = ""
            while plate == "":
                plate = input("Enter license plate: ")
                if plate == "exit":
                    return 1
            result = cursor.execute("SELECT * FROM cars WHERE plate=?", [ plate ]).fetchone()
            if result:
                timestayed = (datetime.now().timestamp() - result[1])/60
                print("You parked here for:", timestayed)
                if timestayed < 10:
                    print("No charge")
                elif timestayed < 30:
                    print("Pay $3")
                else:
                    print("Pay $?", [5 * abs(timestayed/60)])
                cursor.execute("DELETE FROM cars WHERE plate=?", [ plate ])
            else:
                date = datetime.now()
                cursor.execute("""
                INSERT INTO cars(plate, entrytime) VALUES(?,?)
            """, [plate, date.timestamp()])
        except sqlite3.Error as e:
            print(e)

myprogram()
cursor.close()
connection.close()