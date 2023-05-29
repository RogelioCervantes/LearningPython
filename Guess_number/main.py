import random

def guess(x):
    rand_num = random.randint(1, x)
    guess = 0
    while guess != rand_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess < rand_num:
            print("Too low")
        elif guess > rand_num:
            print("Too high")
    print(f"You did it! It was {rand_num}!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high because low = high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?\n--> ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print("Congrats! You coded your first AI!!!")

computer_guess(1000)