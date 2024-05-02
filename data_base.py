from cat_classes import *
from player_class import *
import sqlite3 

def open_database():
    connect = sqlite3.connect("game_database.db")
    cursor = connect.cursor()

    "ДБ для игрока"
    cursor.execute("""CREATE TABLE IF NOT EXISTS players(
                   id INTEGER PRIMARY KEY,
                   name VARCHAR(64))
                """)
    
    "ДБ для котят"
    cursor.execute("""CREATE TABLE IF NOT EXISTS cats(
                   id INTEGER PRIMARY KEY,
                   player_id INTEGER,
                   name VARCHAR(64),
                   age INTEGER,
                   FOREIGN KEY (player_id) REFERENCES players(id))
                   """)

    connect.commit()
    connect.close()

def add_player_to_database(name):
    connect = sqlite3.connect('game_database.db')
    cursor = connect.cursor()

    try:
        cursor.execute("INSERT INTO players (name) VALUES (?)", (name, ))
        connect.commit()
        print("Игрок {0} добавлен в БД".format(name))
    except sqlite3.IntegrityError:
        print("Игрок {0} уже существует".format(name))
    connect.close()

def add_cat_to_database(player_id, name, age):
    connect = sqlite3.connect('game_database.db')
    cursor = connect.cursor()


    cursor.execute("INSERT INTO cats (player_id, name, age) VALUES (?, ?, ?)", (player_id, name, age))
    connect.commit()

    print("Котенок {0} добавлен в БД к игроку с ID".format(name, player_id))

    connect.close()

open_database()