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
            all_cells_indeces = \
                [[square_corner_indeces[0]+row, square_corner_indeces[1]+col] \
                    for col in range(3) for row in range(3)]

        elif which == 'row':
            all_cells_indeces = \
                [[row, x] for x in range(9)]

        elif which == 'col':
            all_cells_indeces = \
                [[y, col] for y in range(9)]

        else:
            raise ValueError('get_indeces(self, row, col, which) must accept \
                a which argument of \'square\', \'row\', or \'col\'. You gave \
                %s' % (which))

        return all_cells_indeces

    def check_by(self, row, col, which):
        current_cell = self.board[row][col]
        if type(current_cell.possible_values) is list:
            all_cells_indeces = self.get_indeces(row, col, which)
            all_cells_indeces.remove([row, col]) # remove current cell
            for other_cell_indeces in all_cells_indeces:
                if type(current_cell.possible_values) is list:
                    other_cell = self.board[other_cell_indeces[0]][other_cell_indeces[1]]
                    current_cell.check(other_cell)
                else:
                    return

    def check_all_once(self, row, col):
        self.check_by(row, col, 'square')
        self.check_by(row, col, 'row')
        self.check_by(row, col, 'col')

    # set cell to a value that doesn't exist elsewhere in
    # its square, column, or row
    def unique_by(self, row, col, which):
        current_cell = self.board[row][col]
        if type(current_cell.possible_values) is list:

            # build a dictionary around current_cell. Look up the count
            # of each value (key) in current_cell. If the dict doesn't contain it,
            # bingo!
            all_cells_indeces = self.get_indeces(row, col, which)
            all_cells_indeces.remove([row, col]) # exclude current_cell

            sure_count_dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
            unsure_count_dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

            for cell_indeces in all_cells_indeces:
                cell_value = self.board[cell_indeces[0]][cell_indeces[1]].possible_values
                if type(cell_value) is int:
                    sure_count_dict[cell_value] += 1
                else:
                    for every_possible_value in cell_value:
                        unsure_count_dict[every_possible_value] += 1

            for value in current_cell.possible_values:
                if sure_count_dict[value] == 0 and unsure_count_dict[value] == 0:
                    current_cell.possible_values = value

    def unique_all_once(self, row, col):
        self.unique_by(row, col, 'square')
        self.unique_by(row, col, 'row')
        self.unique_by(row, col, 'col')

    def run_game(self):

        # while there is any unsure cells
        while any(type(self.board[row][col].possible_values) is list \
            for row in range(9) for col in range(9)):

            for row in range(9):
                for col in range(9):
                    # current_cell = self.board[row][col]
                    self.check_all_once(row, col)
                    self.unique_all_once(row, col)
        # start with a cell
        # check a cell by square, row, column once (check_all_once)
        # check unique for cell

        # go to next cell
        # repeat
        pass

    # print method
    def arrayfy(self):
        board_array = [[None for row in range(9)] for col in range(9)]
        for row in range(9):
            for col in range(9):
                 board_array[row][col] = self.board[row][col].possible_values
                 if board_array[row][col] == range(1,10):
                     board_array[row][col] = 0
        return board_array

    def __str__(self):
        board_array = [[None for row in range(9)] for col in range(9)]
        for row in range(9):
            for col in range(9):
                 board_array[row][col] = self.board[row][col].possible_values
                 if board_array[row][col] == range(1,10):
                     board_array[row][col] = 0
        return '\n'.join(str(x) for x in board_array)
        # return \
        #     '\n'.join([str(self.board[row][col].possible_values) for col in range(9) for row in range[9]])
