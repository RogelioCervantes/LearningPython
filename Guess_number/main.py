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

guess(10)