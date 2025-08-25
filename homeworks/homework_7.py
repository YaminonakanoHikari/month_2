import sqlite3

def create_table():
    conn.execute('''CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    author TEXT,
    publication_year INTEGER,
    genre TEXT,
    number_of_pages INTEGER,
    number_of_copies INTEGER
    )
    ''')

def insert_books(name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute('''INSERT INTO books(name, author, publication_year, 
                                      genre, number_of_pages, number_of_copies) VALUES(?,?,?,?,?,?) 
                 ''', (name, author, publication_year, genre, number_of_pages, number_of_copies))
    conn.commit()





if  __name__ == '__main__':
    conn = sqlite3.connect('data.db')
    insert_books('name', 'author', 56, 'genre', 56, 56)








    create_table()
