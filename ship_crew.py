import sqlite3
import bot

connection = sqlite3.connect('Squids.db')
cursor = connection.cursor()


def create_members_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS members
                    (id int, username TEXT, nickName TEXT)''')
    connection.commit()
    cursor.close()
    connection.close()

def create_movies_on_plex_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS moviesOnPlex
                    (title, rating, onPlex)''')

    connection.commit()
    cursor.close()
    connection.close()

def create_movies_in_queue_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS moviesInQueue
                    (title)''')

    connection.commit()
    cursor.close()
    connection.close()

def load_all_members_in_table():
    

    for guild in bot.bot.guilds:
        for member in guild.members:
            cursor.execute("INSERT INTO members (id, username, nickName) VALUES (?, ?, ?)"),
            (member.id, member.name, member.nick)
    connection.commit()
    cursor.close()
    connection.close()

connection.close()