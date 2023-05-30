import random

def play():
    keepPlaying = ""

    while keepPlaying != 'n':
        user = input("'R' for rock, 'P' for paper, 'S' for scissors\n--> ").lower()
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            print(f"\nYou: {setChoice(user)} // CPU: {setChoice(computer)}\n\nTie.")
        elif is_win(user, computer):
            print(f"\nYou: {setChoice(user)} // CPU: {setChoice(computer)}\n\nYou won!")
        else:
            print(f"\nYou: {setChoice(user)} // CPU: {setChoice(computer)}\n\nYou lost...")
        
        keepPlaying = input("Continue? y/n\n--> ").lower()
    
# R > S, S > P, P > R
def is_win(player, rival):
    # return true if player wins
    if (player == 'r' and rival == 's') \
    or (player == 's' and rival == 'p') \
    or (player == 'p' and rival == 'r'):
        return True
    
def setChoice(choice):
    if choice == 'r':
        return "ROCK"
    elif choice == 'p':
        return "PAPER"
    elif choice == 's': 
        return "SCISSORS"
    else: return "???"
    
play()