import sqlite3

connection = sqlite3.connect('Squids.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE members
                (userID, username)''')

cursor.execute('''CREATE TABLE movies
                (title, rating, onPlex)''')

cursor.execute("INSERT INTO members VALUE ('2006-01-05','BUY','RHAT',100,35.14)")

members = [()]

connection.commit()

connection.close()