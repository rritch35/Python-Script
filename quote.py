#in this script I am going to proivde quotes, then going the python script will select a random quote.
#  I will start with providing the quote then in the future hope to add an api implementation 

import random #going to need random in order to select a random quote


quotes = [
    {"quote": "Any sufficiently advanced technology is indistinguishable from magic.", "author": "Arthur C. Clarke"},
    {"quote": "The best way to predict the future is to invent it.", "author": "Alan Kay"},
    {"quote": "Stay hungry, stay foolish.", "author": "Steve Jobs"}
]
def get_quote():
    return random.choice(quotes)
def display_quote():

    random_quote = random.choice(quotes)
    print(f'"{random_quote["quote"]}"')
    print(f'– {random_quote["author"]}')
display_quote()