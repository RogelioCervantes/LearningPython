import random
from words import words
import string

def getWord(words):
    word = random.choice(words) # choice is for lists
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return words.upper()

def hangman():
    word = getWord(words)
    words_letters = set(word) # letters in the word
    alphabet = set(string.ascii_letters)
    used_letters = set() # what the user has guessed

    # getting user input
    user_letter = input("Guess a letter: ").upper
    if user_letter in alphabet - used_letters:
        used_letters.add(used_letters)
        if user_letter in words_letters:
            words_letters.remove(user_letter)
            
    elif user_letter in used_letters: print("Already used that character. Try again.")
    else: print("Invalid character. Try again.")

user_input = input("Type something: ")
print(user_input)