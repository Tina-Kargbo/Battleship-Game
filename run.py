from random import randint

board = []

for x in range(4):
    board.append([O] * 4)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)