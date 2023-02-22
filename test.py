# import sqlite module
import sqlite3
# connect to sample.db


def connect():
    conn = sqlite3.connect("sample.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

# insert function for book table


def insert(title, author, year, isbn):
    conn = sqlite3.connect("sample.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",
                (title, author, year, isbn))
    conn.commit()
    conn.close()
    view()


# view function
def view():
    conn = sqlite3.connect("sample.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


# connect to sample.db
connect()
insert("The Sun", "John Smith", 1918, 913123132)
insert("The Moon", "John Smooth", 1917, 999999999)
insert("The Earth", "John Smithee", 1919, 888888888)
insert("The Stars", "John Smithy", 1920, 777777777)

print(view())
