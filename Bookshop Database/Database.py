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
        self.conn = sqlite3.connect(f"{self.db_name}")
        self.curs = self.conn.cursor()

        # Create a table
        self.curs.execute("CREATE TABLE IF NOT EXISTS books(\
            title VARCHAR(50),\
            author VARCHAR(50),\
            year INTEGER,\
            isbn INTEGER PRIMARY KEY NOT NULL);")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def get_all(self):
        self.curs.execute("SELECT * FROM books ORDER BY title, year ASC;")
        books = self.curs.fetchall() # List
        return books

    def insert(self, title, author, year, isbn):
        self.curs.execute(f"INSERT INTO books VALUES (\'{title}\', \'{author}\', {year}, {isbn})")
        self.conn.commit()

    def select(self, title='', author='', year=0, isbn=0):
        # Verify inputs
        if year == '':
            select_year = 0
        else:
            select_year = int(year)

        if isbn == '':
            select_isbn = 0
        else:
            select_isbn = int(isbn)

        self.curs.execute(f"SELECT * FROM books WHERE isbn = {select_isbn} \
            OR author = \'{author}\' OR title = \'{title}\' OR year = {select_year};")

        selection = self.curs.fetchall() # List
        return selection

    def delete(self, isbn):
        self.curs.execute(f"DELETE FROM books WHERE isbn={isbn};")
        self.conn.commit()

    def update(self, title, author, year, isbn):
        self.curs.execute(f"UPDATE books SET title=\'{title}\', author=\'{author}\', \
            year={year}, isbn={isbn} WHERE isbn={isbn};")
        self.conn.commit()