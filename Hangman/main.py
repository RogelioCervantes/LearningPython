import random
from words import words

def getWord(words):
    word = random.choice(words) # choice is for lists
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return words.upper()

def hangman():
    word = getWord(words)