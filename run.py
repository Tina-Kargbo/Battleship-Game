import random

    #code referenced from CI lesson on "What are Input Operations?
username = input("Please Type in your Name: ")
print(username)

class Board:
    """User board with grids where the battleship game can be played."""
    def __init__(self, board):
        self.board = board

    #Translates the alphabet to the board numbers to help differentiate rows from columns. 
    def get_alphabet_as_numbers():
        alphabet_as_numbers {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
        return alphabet_as_numbers
    
    def print board(self):
        print("a, b, c, d, e")
        row = 1
        for row in self.board:
            print()


