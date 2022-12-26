import random

    #code referenced from CI lesson on "What are Input Operations?
username = input("Please Type in your Name: ")
print(username)

class Board:
    """User board with grids where the battleship game can be played."""

    def __init__(self, size, ships_num):
        self.size = size
        self.ships = ships_num

MyBoard = Board(5, 4,)
print(self)