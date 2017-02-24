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
    def __init__(self):
        self.board = [[None for row in range(9)] for col in range(9)]
    def __init__(self, init_board):
        self.board = [[None for row in range(9)] for col in range(9)]
        for row in range(9):
            for col in range(9):
                self.board[row][col] = Cell(init_board[row][col])

    def get_indeces(self, row, col, which):
        current_cell = self.board[row][col]

        if which == 'square':
            square_corner_indeces = [row // 3 * 3, col // 3 * 3]
            all_cells_in_square_indeces = \
                [[square_corner_indeces[0]+row, square_corner_indeces[1]+col] \
                    for col in range(3) for row in range(3)]
            return all_cells_in_square_indeces

        elif which == 'row':
            all_cells_in_row_indeces = \
                [[row, x] for x in range(9)]
            return all_cells_in_row_indeces

        elif which == 'col':
            all_cells_in_col_indeces = \
                [[y, col] for y in range(9)]
            return all_cells_in_col_indeces

        else:
            raise ValueError('get_indeces(self, row, col, which) must accept \
                a which argument of \'square\', \'row\', or \'col\'. You gave \
                %s' % (which))

    def check_by(self, row, col, which):
        current_cell = self.board[row][col]
        for other_col in self.get_indeces(row, col, which):
            other_cell = self.board[other_col[0]][other_col[1]]
            current_cell.check(other_cell)


    def check_all_once(self, row, col):
        self.check_by(row, col, 'square')
        self.check_by(row, col, 'row')
        self.check_by(row, col, 'col')

    def unique_square(self, row, col):
        current_cell = self.board[row][col]
        # build a count dictionary

        # for value in current_cell.possible_values:
            # pass
            # for indeces in self.get_indeces(row, col, 'square'):
            #     pass



    def run_game(self):
        #
        pass

    def arrayfy(self):
        board_array = [[None for row in range(9)] for col in range(9)]
        for row in range(9):
            for col in range(9):
                 board_array[row][col] = self.board[row][col].possible_values
                 if board_array[row][col] == range(1,10):
                     board_array[row][col] = 0
        return board_array
