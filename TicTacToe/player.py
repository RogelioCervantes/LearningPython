import math, random

class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\'s turn. Input move (0-9): ")
            # checking if this is a correct value casting it to an integer
            # if it's not, then it's invalid
            # if that spot is not available, it's invalid too
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try agian.")