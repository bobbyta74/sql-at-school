import sqlite3
connection = sqlite3.connect("test.db")

cursor = connection.cursor()
userlist = cursor.execute("select name from users").fetchall()
pwdlist = cursor.execute("select password from users").fetchall()

#Print every entry in database
"""for i in userlist:
    print("\n User", userlist.index(i) + 1)
    print("Username: ", i[0])
    print("Password: ", pwdlist[userlist.index(i)][0])
"""

#Print password when entering username
"""
while True:
    username = input("Enter username: ")
    mytuple = ()
    mytuple += (username,)
    if username == "":
        break
    cursor = connection.cursor()
    try:
        print("The password for", username, "is", pwdlist[userlist.index(mytuple)][0])
    except sqlite3.Error as e:
        print(e)
    cursor.close()
connection.close()
"""

#Check password for username
"""
while True:
    username = input("Enter username: ")
    utuple = ()
    utuple += (username,)
    if username == "":
        break
    password = input("Enter username: ")
    ptuple = ()
    ptuple += (password,)
    cursor = connection.cursor()
    try:
        if password == pwdlist[userlist.index(utuple)][0]:
            print("Correct")
        else:
            print("You are wrong.")
    except sqlite3.Error as e:
        print(e)
    cursor.close()
connection.close()
"""

#Make new account
"""
while True:
    username = input("Enter username: ")
    if username == "":
        break
    password = input("Enter username: ")
    cursor = connection.cursor()
    try:
        
    except sqlite3.Error as e:
        print(e)
    cursor.close()
connection.close()
"""