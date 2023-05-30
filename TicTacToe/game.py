class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # this is the 3x3 board
        self.current_winer = None # keeps track of the winner

                