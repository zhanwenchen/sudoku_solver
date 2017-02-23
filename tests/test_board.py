from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

from board import Board
from cell import Cell
sys.path.pop(0)

# import board

board_init_1 = \
    [[0, 9, 1, 2, 0, 0, 0, 0, 4], \
     [8, 0, 0, 6, 0, 0, 0, 0, 0], \
     [0, 0, 4, 1, 5, 0, 0, 0, 0], \
     [4, 0, 0, 9, 0, 0, 2, 0, 8], \
     [9, 7, 0, 0, 0, 0, 0, 0, 1], \
     [0, 0, 2, 5, 1, 0, 6, 0, 0], \
     [0, 0, 0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 8, 0, 6, 4, 1, 0], \
     [0, 0, 0, 0, 0, 0, 0, 5, 0]]

e = range(1,10) # empty becomes [1,2,3,4,5,6,7,8,9]. This saves time and space
board_expected_1 = \
    [[0, 9, 1, 2, 0, 0, 0, 0, 4], \
     [8, 0, 0, 6, 0, 0, 0, 0, 0], \
     [0, 0, 4, 1, 5, 0, 0, 0, 0], \
     [4, 0, 0, 9, 0, 0, 2, 0, 8], \
     [9, 7, 0, 0, 0, 0, 0, 0, 1], \
     [0, 0, 2, 5, 1, 0, 6, 0, 0], \
     [0, 0, 0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 8, 0, 6, 4, 1, 0], \
     [0, 0, 0, 0, 0, 0, 0, 5, 0]]

# Testing __init__
#
# board_result_1 = Board(board_init_1).arrayfy()
# for row in board_result_1:
#     for col in row:
#         print(col)
#     print()

board_object_1 = Board(board_init_1)

test_init_1 = \
    board_object_1.arrayfy() == board_expected_1

# print(test_init_1)

print('Test 1 passed' if test_init_1 else 'Test 1 failed')


# Testing check_square
print(board_object_1.arrayfy())
board_object_1.check_square(0, 0)
print(board_object_1.arrayfy())
# print(board_object_1.board[0][0].getValue())
test_check_square_1 = \
    board_object_1.board[0][0].possible_values == [2,3,5,6,7]
print('Test 2 passed' if test_check_square_1 else 'Test 2 failed')

print(board_object_1.board[6][6].possible_values)
board_object_1.check_square(6, 6)
print(board_object_1.board[6][6].possible_values)
test_check_square_2 = \
    board_object_1.board[6][6].possible_values == [2,3,6,7,8,9]
print('Test 3 passed' if test_check_square_2 else 'Test 3 failed')


# Testing checkRow
print(board_object_1.board[5][5].possible_values)
board_object_1.check_row(5, 5)
print(board_object_1.board[5][5].possible_values)
test_check_row_1 = \
    board_object_1.board[5][5].possible_values == [3,4,7,8,9]
print('Test 4 passed' if test_check_row_1 else 'Test 4 failed')

# Testing checkColumn
