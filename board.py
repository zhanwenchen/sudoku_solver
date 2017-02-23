# or take out from a bag, with a singleton array being a certain cell

# 1. check for each cell
# a. check square
# b. check row
# c. check column
# d. if every cell in square/row/column has an array, check for uniqueness for all numbers. if a number hasn't appeared yet, that's it!
# if ok, append to possible array

# heuristic
# while calculate most (square + row + column) that is unique (2 for column and 2 for row is the same)
# 1. start with cell with most (square + row + column)
# 2. if can figure out unique, check for conflict, and go to most (square + row + column)

from cell import Cell

index_range = range(9)

class Board:
    board = [[None for row in index_range] for col in index_range]
    def __init__(self, init_board):
        for row in index_range:
            for col in index_range:
                self.board[row][col] = Cell(init_board[row][col])
                # print('board[%s][%s] is set to %s' % (row, col, self.board[row][col]))

    def check_square(self, row, col):
        current_cell = self.board[row][col]
        square_corner_indeces = [row // 3 * 3, col // 3 * 3]
        all_cells_in_square_indeces = \
            [[square_corner_indeces[0]+i, square_corner_indeces[1]+j] \
                for j in range(3) for i in range(3)]
        print(all_cells_in_square_indeces)
        all_cells_in_square_indeces.remove([row, col])
        for other_cell_indeces in all_cells_in_square_indeces:
            other_cell = self.board[other_cell_indeces[0]][other_cell_indeces[1]]
            current_cell.check(other_cell)

    def check_row(self, row):
        if row in index_range:

        else:
            raise ValueError('check_row(): invalid row number %s given' % (row))

    def arrayfy(self):
        board_array = [[None for row in index_range] for col in index_range]
        for row in index_range:
            for col in index_range:
                 board_array[row][col] = self.board[row][col].getValue()
        return board_array
