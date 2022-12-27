from random import randint

board = []

for x in range(4):
    board.append(["O"] *4)

def print_board(board):
    for row in board:
        print_board(board)

def random_row(board):
    return randint(0, len(board[0]) - 1)

def random_column(board):
    return randint(0, len(board[0]) - 1)

grid_row = random_row(board)
grid_column = random_column(board)

print(grid_row)
print(grid_column)