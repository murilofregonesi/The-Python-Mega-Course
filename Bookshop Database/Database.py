"""
Bookshop Database - Database

Created on December 2020
@author: Murilo Fregonesi Falleiros
"""

import sqlite3

class Database:

    def __init__(self, file_name):

        # Create or access the Database
        self.db_name = file_name
        conn = sqlite3.connect(f"{self.db_name}")
        curs = conn.cursor()

        # Create a table
        curs.execute("CREATE TABLE IF NOT EXISTS books(\
            title VARCHAR(50),\
            author VARCHAR(50),\
            year INTEGER,\
            isbn INTEGER PRIMARY KEY NOT NULL);")
        conn.commit()
        conn.close()

    def get_all(self):
        conn = sqlite3.connect(f"{self.db_name}")
        curs = conn.cursor()

        curs.execute("SELECT * FROM books ORDER BY title, year ASC;")
        books = curs.fetchall() # List

        conn.close()
        return books

    def insert(self, title, author, year, isbn):
        conn = sqlite3.connect(f"{self.db_name}")
        curs = conn.cursor()

        curs.execute(f"INSERT INTO books VALUES (\'{title}\', \'{author}\', {year}, {isbn})")
        conn.commit()
        conn.close()

    def select(self, title='', author='', year=0, isbn=0):
        conn = sqlite3.connect(f"{self.db_name}")
        curs = conn.cursor()

        # Verify inputs
        if year == '':
            select_year = 0
        else:
            select_year = int(year)

        if isbn == '':
            select_isbn = 0
        else:
            select_isbn = int(isbn)

        curs.execute(f"SELECT * FROM books WHERE isbn = {select_isbn} \
            OR author = \'{author}\' OR title = \'{title}\' OR year = {select_year};")

        selection = curs.fetchall() # List
        conn.close()
        return selection

    def delete(self, isbn):
        conn = sqlite3.connect(f"{self.db_name}")
        curs = conn.cursor()

        curs.execute(f"DELETE FROM books WHERE isbn={isbn};")

        conn.commit()
        conn.close()

    def update(self, title, author, year, isbn):
        conn = sqlite3.connect(f"{self.db_name}")
        curs = conn.cursor()

        curs.execute(f"UPDATE books SET title=\'{title}\', author=\'{author}\', \
            year={year}, isbn={isbn} WHERE isbn={isbn};")

        conn.commit()
        conn.close()