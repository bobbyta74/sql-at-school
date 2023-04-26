import csv
import sqlite3

connection = sqlite3.connect("games.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS games;")

cursor.execute("""
    CREATE TABLE games(
        game_id integer PRIMARY KEY,
        title text,
        released text,
        team text,
        rating real,
        reviews integer,
        genres text,
        UNIQUE (title)
    );""")
#game_id INTEGER PRIMARY KEY,);

with open("games.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    headings = next(csv_reader)
    for row in csv_reader:
        title, released, team, rating, reviews, genres = row
        
        #Converts date into time in seconds since 1970
        dt = datetime.datetime.strptime("released", "%d-%b-%y")

        cursor.execute("""
            INSERT OR IGNORE INTO games(title, released, team, rating, reviews, genres) VALUES(?,?,?,?,?,?)
        """, [ title, released, team, rating, reviews, genres ])
connection.commit()
cursor.close()    
connection.close()



