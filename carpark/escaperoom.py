import sqlite3
from datetime import datetime, date

connection = sqlite3.connect("bookings.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE bookings")

try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings(
            id integer PRIMARY KEY,
            name text,
            session text,
            date text
        );""")
except sqlite3.Error as e:
    print(e)

bookdate1 = date(2001, 9, 11)
session = ""
def inputdetails():
    bookdate = ""
    while bookdate == "" or len(bookdate) != 10:
        bookdate = input("Select date (dd/mm/yy): ")
    bookdate1 = date(int(bookdate[6:10]), int(bookdate[3:5]), int(bookdate[0:2]))
    while bookdate1.strftime("%A") == "Monday" or bookdate1.strftime("%A") == "Thursday":
        print("The escape room is closed on Mondays and Thursdays.")
        bookdate = input("Select date (dd/mm/yy): ")
    bookdate1 = date(int(bookdate[6:10]), int(bookdate[3:5]), int(bookdate[0:22]))
    session = input("Choose a session (morning/afternoon/evening): ")

def myprogram():
    while True:
        try:
            inputdetails()
            #Check if session is booked on that day
            result = cursor.execute("SELECT * FROM bookings WHERE date=? AND session=?", [ bookdate1, session ]).fetchone()
            while result:
                print("That session is already taken.")
                inputdetails()
                result = cursor.execute("SELECT * FROM bookings WHERE date=? AND session=?", [ bookdate1, session ]).fetchone()
            cursor.execute("""
                INSERT INTO bookings(name, session, date) VALUES(?,?,?)
            """, [input("Enter name: "), session, bookdate1])

        except sqlite3.Error as e:
            print(e)

myprogram()
cursor.close()
connection.close()