"""
English Thesaurus - MySQL Version

Created on November 2020
@author: Murilo Fregonesi Falleiros
"""

import mysql.connector as mysql

# Create a connection to the DataBase
connector = mysql.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)
cursor = connector.cursor() # Create a Cursor

word = input('Enter an word: ') # Input

query = cursor.execute(f'SELECT * FROM Dictionary WHERE Expression = \'{word}\'') # Execute a Query
results = cursor.fetchall() # Get results as a list of tuples

if results:
    for result in results:
        print(result[1])
else:
    print('Word was not found.')

''' TODO
1. Verify similarity
2. Handle input (lower or title letters)
3. Loop script (with exit)
'''