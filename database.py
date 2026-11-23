import sqlite3
from datetime import datetime


def connect_db():
    return sqlite3.connect("searches.db")


def create_table():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            search_date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_search(username):
    connection = connect_db()
    cursor = connection.cursor()

    search_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO search_history (username, search_date)
        VALUES (?, ?)
    """, (username, search_date))

    connection.commit()
    connection.close()


def view_history():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM search_history
        ORDER BY id DESC
    """)

    history = cursor.fetchall()
    connection.close()

    return history