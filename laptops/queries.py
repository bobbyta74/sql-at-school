import sqlite3

connection = sqlite3.connect("laptops.db")

while True:
    sql = input("SQL: ")
    if sql == "":
        break
    cursor = connection.cursor()
    try:
        results = cursor.execute(sql)
        for row in results:
            print(row)
    except sqlite3.Error as e:
        print(e)
    cursor.close()
connection.close()
    

connection.close()

#SELECT * FROM laptops
#SELECT Company, TypeName FROM laptops WHERE TouchScreen=1
#SELECT * FROM laptops WHERE resolution_width>1920
#SELECT CompanyName, Price WHERE TypeName="Gaming" AND Ram=16 AND ssd=256
#SELECT * FROM laptops order by Price desc limit 1
#SELECT * FROM laptops WHERE TypeName="Ultrabook" AND Price>30000 AND Price<40000