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

class Board:
    # board = [[None for row in index_range] for col in index_range]
    def __init__(self):
        self.board = [[None for row in range(9)] for col in range(9)]
    def __init__(self, init_board):
        # self.board = [[Cell(init_board[row][col]) for col in index_range] for row in index_range]
        self.board = [[None for row in range(9)] for col in range(9)]
        for row in range(9):
            for col in range(9):
                self.board[row][col] = Cell(init_board[row][col])
                # print('self.board[%s][%s] = Cell(init_board[row][col]) = %s' % (row, col, self.board[row][col]))
                # print('board[%s][%s] is set to %s' % (row, col, self.board[row][col]))

    def check_square(self, row, col):
        current_cell = self.board[row][col]
        # print('current_cell [%s][%s] = %s' % (row, col, current_cell))
        # print('before checking, current_cell [%s][%s] contains %s' \
            # % (row, col, current_cell.possible_values))
        # the top left cell of the square where current_cell resides
        square_corner_indeces = [row // 3 * 3, col // 3 * 3]
        # print('current cell [%s][%s] belong to square [%s][%s]' \
            # % (row, col, square_corner_indeces[0], square_corner_indeces[1]))
        all_cells_in_square_indeces = \
            [[[square_corner_indeces[0]+row, square_corner_indeces[1]+col] \
                for col in range(3)] for row in range(3)]
        # all_cells_in_square_indeces.remove([row, col])
        # print('the other cells in the square are %s ' % all_cells_in_square_indeces)
        for other_row in all_cells_in_square_indeces:
            for other_col in other_row:
                # print('other_row is %s. other_col is %s' % (other_row, other_col))
                other_cell = self.board[other_col[0]][other_col[1]]
                # print('checking current_cell against [%s][%s]' % (other_col[0], other_col[1]))
                current_cell.check(other_cell)

    def check_row(self, row, col):
        current_cell = self.board[row][col]
        row_head_indeces = [row, 0]
        all_cells_in_row_indeces = \
            [[row, x] for x in range(9)]

        for other_col in all_cells_in_row_indeces:
            # print('other_row is %s. other_col is %s' % (other_row, other_col))
            other_cell = self.board[other_col[0]][other_col[1]]
            # print('checking current_cell against [%s][%s]' % (other_col[0], other_col[1]))
            current_cell.check(other_cell)

    def check_col(self, row, col):
        current_cell = self.board[row][col]
        col_head_indeces = [0,col]
        all_cells_in_col_indeces = \
            [[y, col] for y in range(9)]

        for other_col in all_cells_in_col_indeces:
            # print('other_row is %s. other_col is %s' % (other_row, other_col))
            other_cell = self.board[other_col[0]][other_col[1]]
            # print('checking current_cell against [%s][%s]' % (other_col[0], other_col[1]))
            current_cell.check(other_cell)

    def arrayfy(self):
        board_array = [[None for row in range(9)] for col in range(9)]
        for row in range(9):
            for col in range(9):
                 board_array[row][col] = self.board[row][col].possible_values
                 if board_array[row][col] == range(1,10):
                     board_array[row][col] = 0
        return board_array
