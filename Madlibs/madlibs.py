# string concatenation (aka how to put strings together)

#food = "hamburger"

#print("I would like a " + food)
#print("I would like a {}".format(food))
#print(f"I would like a {food}") # this one is the best (imo)

someWord = input("Type something: ")
someWord2 = input("Type something again: ")

madlib = f"This is what you typed first: {someWord}\
    \nAnd this is what you typed next: {someWord2}"

print(madlib)