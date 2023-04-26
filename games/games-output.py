import sqlite3
import os

#Output games with >3000 reviews
def query1(dbname):
    connection = sqlite3.connect(dbname)

    #sql = "SELECT * FROM games WHERE reviews > 3000;"
    sql = "SELECT * FROM games"
    cursor = connection.cursor()
    try:
        results = cursor.execute(sql)
        for row in results: print(list(row))
    except sqlite3.Error as e:
        print(e)
    cursor.close()
        
    connection.close()

#Count Konami games
def query2(dbname):
    connection = sqlite3.connect(dbname)
    counter = 0
    sql = "SELECT * FROM games WHERE team = 'Konami';"
    cursor = connection.cursor()
    try:
        results = cursor.execute(sql)
        for row in results: 
            print(list(row))
            counter += 1
        print("Games made by Konami:", counter)
    except sqlite3.Error as e:
        print(e)
    cursor.close()
        
    connection.close()

#Avg rating
def query3(dbname):
    connection = sqlite3.connect(dbname)
    sql = "SELECT sum(rating)/count(rating) FROM games;"
    cursor = connection.cursor()
    try:
        results = cursor.execute(sql).fetchone()
        print(results[0])
    except sqlite3.Error as e:
        print(e)
    cursor.close()
        
    connection.close()

#Output RPGs
def query4(dbname):
    connection = sqlite3.connect(dbname)
    sql = "SELECT * FROM games WHERE genres LIKE '%RPG%';"
    cursor = connection.cursor()
    try:
        results = cursor.execute(sql)
        for row in results: 
            print(list(row))
    except sqlite3.Error as e:
        print(e)
    cursor.close()
        
    connection.close()

#Output 2022 releases
def query5(dbname):
    connection = sqlite3.connect(dbname)
    sql = "SELECT * FROM games WHERE released LIKE '%22';"
    cursor = connection.cursor()
    try:
        results = cursor.execute(sql)
        for row in results: 
            print(list(row))
    except sqlite3.Error as e:
        print(e)
    cursor.close()
        
    connection.close()

dbname = "games.db"
if not dbname.endswith(".db"):
    dbname += ".db"
if os.path.exists(dbname):
    query1(dbname)
    query2(dbname)
    query3(dbname)
    query4(dbname)
    query5(dbname)
else:
    print(f"Database not found: {dbname}")


