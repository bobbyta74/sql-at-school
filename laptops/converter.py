import csv
import sqlite3

connection = sqlite3.connect("laptops.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS laptops;")

cursor.execute("""
    CREATE TABLE laptops(
        indx integer primary key,
        Company text,
        TypeName text,
        Inches real,
        touchscreen bool,
        retinadisplay bool,
        resolution_width integer,
        cpu_Speed real,
        Ram integer,
        ssd integer,
        Price integer
        );
    """)

with open("laptops.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    headings = next(csv_reader)
    for row in csv_reader:
        cursor.execute("""
            INSERT INTO laptops VALUES(?,?,?,?,?,?,?,?,?,?,?)
        """, row)
        
connection.commit()
cursor.close()    
connection.close()



