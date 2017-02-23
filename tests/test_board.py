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

e = range(1,10)
board_expected_1 = \
    [[e, 9, 1, 2, e, e, e, e, 4], \
     [8, e, e, 6, e, e, e, e, e], \
     [e, e, 4, 1, 5, e, e, e, e], \
     [4, e, e, 9, e, e, 2, e, 8], \
     [9, 7, e, e, e, e, e, e, 1], \
     [e, e, 2, 5, 1, e, 6, e, e], \
     [e, e, e, e, e, e, e, e, e], \
     [e, e, e, 8, e, 6, 4, 1, e], \
     [e, e, e, e, e, e, e, 5, e]]

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

board_object_1.check_square(0, 0) # expect [0][0] to be [2,3,5,6,7]
# print(board_object_1.board[0][0].getValue())
test_check_square_1 = \
    board_object_1.board[0][0].getValue() == [2,3,5,6,7]
print('Test 2 passed' if test_check_square_1 else 'Test 2 failed')

# Testing checkRow

# Testing checkColumn
