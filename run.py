import random

class GridBoard:
    def __init__(self, grid):
        self.board 

    def print_board(self):
        row_number = 1
        for row in self.board:
            print(row_number, ".".join(row))
            row_number +=1