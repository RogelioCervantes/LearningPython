import random
from words import words
import string

def getWord(w):
    word = random.choice(w) # choice is for lists
    while '-' in word or ' ' in word:
        word = random.choice(w)

    return word.upper()

def hangman():
    word = getWord(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_letters)
    used_letters = set() # what the user has guessed

    lives = 6

    

    # finishes the loop when there's no more letters to guess
    while len(word_letters) > 0 and lives > 0:
        # Current word.
        # replaces the letters that haven't been guessed
        # with an underscore (W _ R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("\nCurrent word: ", " ".join(word_list))

        guessed_letter = input("Guess a letter: ").upper()
        if guessed_letter in alphabet - used_letters:
            used_letters.add(guessed_letter)
            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)
                print("Correct!")
            else:
                lives -= 1
                print("Incorrect.")
                
        elif guessed_letter in used_letters: 
            print("Already used that character. Try again.")
        else:
            print("Invalid character. Try again.")
        
        # Letters used.
        # join() turns used_letters into a string separated by 
        # whatever is before it, in this case a blank space.
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(f"Attempts left: {lives}\nYou have used these letters: ", " ".join(used_letters))
    
    # After the loop.
    if lives == 0:
        print(f"\nYou died. The word was {word}")
    else:
        print(f"\nYou made it! The word was {word}")

hangman()