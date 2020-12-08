"""
Bookshop Database - GUI

Created on December 2020
@author: Murilo Fregonesi Falleiros
"""

import Database
from tkinter import *

class Window:

    def __init__(self, database):

        self.window = Tk() # Create main window
        self.window.title('Bookshop Database')
        self.database = database # Reference database

        # Buttons Configuration

        btn_column = 4 # Position
        btn_width = 15 # Width

        btn_view = Button(self.window, text='View All', command=self.view_all, width=btn_width)
        btn_view.grid(column=btn_column, row=3)

        btn_search = Button(self.window, text='Search Entry', command=self.search, width=btn_width)
        btn_search.grid(column=btn_column, row=4)

        btn_add = Button(self.window, text='Add Entry', command=self.add, width=btn_width)
        btn_add.grid(column=btn_column, row=5)

        btn_update = Button(self.window, text='Update Selected', command=self.update, width=btn_width)
        btn_update.grid(column=btn_column, row=6)

        btn_del = Button(self.window, text='Delete Selected', command=self.delete, width=btn_width)
        btn_del.grid(column=btn_column, row=7)

        btn_close = Button(self.window, text='Close', command=self.close, width=btn_width)
        btn_close.grid(column=btn_column, row=8)

        # Labels Configuration

        lbl_width = 10 # Width

        lbl_title = Label(self.window, text='Title', width=lbl_width)
        lbl_title.grid(column=0, row=0)

        lbl_title = Label(self.window, text='Year', width=lbl_width)
        lbl_title.grid(column=0, row=1)

        lbl_title = Label(self.window, text='Author', width=lbl_width)
        lbl_title.grid(column=2, row=0)

        lbl_title = Label(self.window, text='ISBN', width=lbl_width)
        lbl_title.grid(column=2, row=1)

        # Entries Configuration

        entry_width = 15 # Width

        self.entry_title = Entry(self.window, width=entry_width)
        self.entry_title.grid(column=1, row=0)
        
        self.entry_year = Entry(self.window, width=entry_width)
        self.entry_year.grid(column=1, row=1)
        
        self.entry_author = Entry(self.window, width=entry_width)
        self.entry_author.grid(column=3, row=0)
        
        self.entry_isbn = Entry(self.window, width=entry_width)
        self.entry_isbn.grid(column=3, row=1)
        
        # ListBox Configuration

        self.list_res = Listbox(self.window, height=8, width=35)
        self.list_res.grid(column=0, row=2, columnspan=4, rowspan=8)

        self.scroll = Scrollbar(self.window)
        self.scroll.grid(column=3, row=2, rowspan=8)

        # Configure the scroll bar and listbox connection
        self.list_res.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.list_res.yview)

        # Configure Listbox event
        self.list_res.bind('<<ListboxSelect>>', self.get_selection)

        self.window.mainloop() # Maintain window open

    # Functions

    def view_all(self):
        # Get the books
        books = self.database.get_all()

        # Insert into Listbox
        self.list_clear()
        for book in books:
            self.list_insert(book)

    def view(self, list):
        # Insert into Listbox
        self.list_clear()
        for book in list:
            self.list_insert(book)

    def search(self):
        # Get entries
        title = self.entry_title.get()
        author = self.entry_author.get()
        year = self.entry_year.get()
        isbn = self.entry_isbn.get()

        # Update the database and the listbox
        selection = self.database.select(title, author, year, isbn)
        self.view(selection)

    def add(self):
        # Get entries
        title = self.entry_title.get()
        author = self.entry_author.get()
        year = int(self.entry_year.get())
        isbn = int(self.entry_isbn.get())
        
        # Update the database and the listbox
        self.database.insert(title, author, year, isbn)
        self.view_all()

    def update(self):
        title, author, year, isbn = selected_item

        title = self.entry_title.get()
        author = self.entry_author.get()
        year = int(self.entry_year.get())

        self.database.update(title, author, int(year), int(isbn))
        self.view_all()

    def delete(self):
        title, author, year, isbn = selected_item
        self.database.delete(int(isbn))
        self.view_all()

    def close(self):
        print('Closed by the user.')
        self.window.quit()

    def entry_replace(self, entry, text):
        entry.delete(0, END)
        entry.insert(END, text)

    def list_insert(self, entry):
        self.list_res.insert(END, entry)

    def list_clear(self):
        self.list_res.delete(0, END)

    def get_selection(self, event):
        if len(self.list_res.curselection()) < 1:
            return
        
        index = self.list_res.curselection()[0]
        global selected_item
        selected_item = self.list_res.get(index)
        
        title, author, year, isbn = selected_item

        self.entry_replace(self.entry_title, title)
        self.entry_replace(self.entry_author, author)
        self.entry_replace(self.entry_year, str(year))
        self.entry_replace(self.entry_isbn, str(isbn))