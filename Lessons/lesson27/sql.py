import sqlite3

FILENAME = "D:/DATABASE/database_sql/data.db"

connection = sqlite3.connect(FILENAME)
cursor_ = connection.cursor()

cursor_.execute("""CREATE TABLE books (id, name, author, price);""")

connection.commit()

cursor_.close()