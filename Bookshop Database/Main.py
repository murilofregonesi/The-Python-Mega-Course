"""
Bookshop Database - Database

Created on December 2020
@author: Murilo Fregonesi Falleiros
"""

import Bookshop # Our GUI Class
import Database # Our Database Class

if __name__ == '__main__': # Direct script call

    database = Database.Database('bookshop')
    window = Bookshop.Window(database)