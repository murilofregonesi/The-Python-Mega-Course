"""
Bookshop Database

Created on December 2020
@author: Murilo Fregonesi Falleiros
"""

from tkinter import *

class Window:

    def __init__(self):

        self.window = Tk() # Create main window

        # Buttons Configuration

        btn_column = 4 # Position
        btn_width = 15 # Width

        btn_view = Button(self.window, text='View All', command=self.click, width=btn_width)
        btn_view.grid(column=btn_column, row=3)

        btn_search = Button(self.window, text='Search Entry', command=self.click, width=btn_width)
        btn_search.grid(column=btn_column, row=4)

        btn_add = Button(self.window, text='Add Entry', command=self.click, width=btn_width)
        btn_add.grid(column=btn_column, row=5)

        btn_update = Button(self.window, text='Update Selected', command=self.click, width=btn_width)
        btn_update.grid(column=btn_column, row=6)

        btn_del = Button(self.window, text='Delete Selected', command=self.click, width=btn_width)
        btn_del.grid(column=btn_column, row=7)

        btn_close = Button(self.window, text='Close', command=self.click, width=btn_width)
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

        entry_title = Entry(self.window, width=entry_width)
        entry_title.grid(column=1, row=0)
        
        entry_year = Entry(self.window, width=entry_width)
        entry_year.grid(column=1, row=1)
        
        entry_author = Entry(self.window, width=entry_width)
        entry_author.grid(column=3, row=0)
        
        entry_isbn = Entry(self.window, width=entry_width)
        entry_isbn.grid(column=3, row=1)
        
        # ListBox Configuration

        self.list_res = Listbox(self.window, height=8, width=45)
        self.list_res.grid(column=0, row=2, columnspan=4, rowspan=8)

        self.window.mainloop() # Maintain window open

    # Functions

    def click(self):
        print('Missing function connection')

    def entry_replace(self, entry, text):
        entry.delete(0, END)
        entry.insert(END, text)

    def entry_get(self, entry):
        return entry.get()

    def list_insert(self, entry):
        self.list_res.insert(END, entry)

    def list_clear(self):
        self.list_res.delete(0, END)

# At a direct Script call
if __name__ == '__main__':
    window = Window()