import sqlite3

connection = sqlite3.connect("telbotdb.db")
cursor = connection.cursor()


def initiate_db(connection, cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL DEFAULT 1000
    );""")
    """
    cursor.execute("INSERT INTO Products (title, description, price) VALUES(?, ?, ?)",
                   ("Продукт 1", "Свёкла", "100"))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES(?, ?, ?)",
                   ("Продукт 2", "Огурец", "200"))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES(?, ?, ?)",
                   ("Продукт 3", "Дыня", "300"))
    cursor.execute("INSERT INTO Products (title, description, price) VALUES(?, ?, ?)",
                   ("Продукт 4", "Помидор", "400"))
    connection.commit()
    """


def add_user(username, email, age, connection, cursor):
    cursor.execute("""
    INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?);""",(username, email, age, 1000))
    connection.commit()


def is_included(username, connection, cursor):
    cursor.execute("""
    SELECT COUNT(*) FROM Users WHERE username = ?;""", (username,))
    count = cursor.fetchone()[0]
    connection.commit()
    return count > 0


def get_all_products(connection, cursor):
    cursor.execute("SELECT id, title, description, price FROM Products;")
    connection.commit()
    return cursor.fetchall()


connection.commit()
connection.close()
