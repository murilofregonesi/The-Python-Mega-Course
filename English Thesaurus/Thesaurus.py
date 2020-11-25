"""
English Thesaurus

Created on November 2020
@author: Murilo Fregonesi Falleiros
"""

# Import Thesaurus Dataset
import json
data = json.load(open('data.json')) # Dictionary from JSON

# Thesaurus
def WordThesaurus(word):
    # Try to find the word
    if word in data.keys():
        print('\n'.join(data[word]))
    elif word.lower() in data.keys():
        print('\n'.join(data[word.lower()]))
    else: # Find word Matches
        GetMatches(word.lower())

# Verify Best Matches
from difflib import get_close_matches as matches

def GetMatches(word):
    matches_list = matches(word, data.keys(), n=1) # All matches

    if len(matches_list) > 0:
        answer = input(f'Did you mean \'{matches_list[0]}\'? [y/n] ')
        if answer == 'y':
            print('\n'.join(data[matches_list[0]]))
        else:
            print('There is no such word.')
    else:
        print('There is no such word.')

# Main
while True:
    word = input('Enter an word (\'q\' to Quit): ') # Input Handling
    if word == 'q':
        break
    else:
        WordThesaurus(word)