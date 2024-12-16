import sqlite3

connection = sqlite3.connect("telbotdb.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
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

def get_all_products(connection, cursor):
    cursor.execute("SELECT id, title, description, price FROM Products;")
    connection.commit()
    return cursor.fetchall()

connection.commit()
connection.close()