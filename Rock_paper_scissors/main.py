import random

def play():
    print("'R' for rock, 'P' for paper, 'S' for scissors, 'E' for exit")
    user = ""

    while user != 'e':
        user = input("--> ").lower
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            print(f"You: {setChoice(user)} // CPU: {setChoice(computer)}\nTie.")
        elif is_win(user, computer):
            print(f"You: {setChoice(user)} // CPU: {setChoice(computer)}\nYou won!")
        else:
            print(f"You: {setChoice(user)} // CPU: {setChoice(computer)}\nYou lost...")
    
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