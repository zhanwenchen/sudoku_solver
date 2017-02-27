from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

from board import Board
from cell import Cell
sys.path.pop(0)

# import board

board_init_1 = \
    [[0, 9, 1,    2, 0, 0,    0, 0, 4], \
     [8, 0, 0,    6, 0, 0,    0, 0, 0], \
     [0, 0, 4,    1, 5, 0,    0, 0, 0], \

     [4, 0, 0,    9, 0, 0,    2, 0, 8], \
     [9, 7, 0,    0, 0, 0,    0, 0, 1], \
     [0, 0, 2,    5, 1, 0,    6, 0, 0], \

     [0, 0, 0,    0, 0, 0,    0, 0, 0], \
     [0, 0, 0,    8, 0, 6,    4, 1, 0], \
     [0, 0, 0,    0, 0, 0,    0, 5, 0]]

e = range(1,10) # empty becomes [1,2,3,4,5,6,7,8,9]. This saves time and space
board_expected_1 = \
    [[0, 9, 1,    2, 0, 0,    0, 0, 4], \
     [8, 0, 0,    6, 0, 0,    0, 0, 0], \
     [0, 0, 4,    1, 5, 0,    0, 0, 0], \

     [4, 0, 0,    9, 0, 0,    2, 0, 8], \
     [9, 7, 0,    0, 0, 0,    0, 0, 1], \
     [0, 0, 2,    5, 1, 0,    6, 0, 0], \

     [0, 0, 0,    0, 0, 0,    0, 0, 0], \
     [0, 0, 0,    8, 0, 6,    4, 1, 0], \
     [0, 0, 0,    0, 0, 0,    0, 5, 0]]

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
# print(board_object_1.arrayfy())
board_object_1.check_by(0, 0, 'square')
# print(board_object_1.arrayfy())
# print(board_object_1.board[0][0].getValue())
test_check_square_1 = \
    board_object_1.board[0][0].possible_values == [2,3,5,6,7]
print('Test 2 passed' if test_check_square_1 else 'Test 2 failed')

# print(board_object_1.board[6][6].possible_values)
board_object_1.check_by(6, 6, 'square')
# print(board_object_1.board[6][6].possible_values)
test_check_square_2 = \
    board_object_1.board[6][6].possible_values == [2,3,6,7,8,9]
print('Test 3 passed' if test_check_square_2 else 'Test 3 failed')


# Testing checkRow
# print(board_object_1.board[5][5].possible_values)
board_object_1.check_by(5, 5, 'row')
# print(board_object_1.board[5][5].possible_values)
test_check_row_1 = \
    board_object_1.board[5][5].possible_values == [3,4,7,8,9]
print('Test 4 passed' if test_check_row_1 else 'Test 4 failed')

# Testing checkColumn
# print(board_object_1.board[4][4].possible_values)
board_object_1.check_by(4, 4, 'col')
# print(board_object_1.board[4][4].possible_values)
test_check_col_1 = \
    board_object_1.board[4][4].possible_values == [2,3,4,6,7,8,9]
print('Test 5 passed' if test_check_col_1 else 'Test 5 failed')

# Testing check_all
# print(board_object_1.board[3][4].possible_values)
board_object_1.check_all_once(3, 4)
# print(board_object_1.board[3][4].possible_values)
test_check_all_once_1 = \
    board_object_1.board[3][4].possible_values == [3,6,7]
print('Test 6 passed' if test_check_all_once_1 else 'Test 6 failed')






####################### Testing unique_by #####################################

board_init_2 = \
    [[0, 9, 1,    2, 0, 0,    0, 0, 4], \
     [8, 0, 0,    6, 0, 0,    1, 0, 0], \
     [0, 0, 4,    1, 5, 0,    0, 0, 0], \

     [4, 1, 5,    9, 0, 0,    2, 0, 8], \
     [9, 7, 6,    0, 0, 0,    5, 0, 1], \
     [0, 8, 2,    5, 1, 0,    6, 0, 0], \

     [0, 0, 0,    0, 0, 0,    0, 0, 0], \
     [0, 0, 0,    8, 0, 6,    4, 1, 0], \
     [0, 0, 0,    0, 0, 0,    0, 5, 0]]

board_object_2 = Board(board_init_2)

# print(board_object_2.board[5][0].possible_values)
board_object_2.unique_by(5, 0, 'square')
# print(board_object_2.board[5][0].possible_values)
test_unique_by_1 = \
    board_object_2.board[5][0].possible_values == 3
print('Test 7 passed' if test_unique_by_1 else 'Test 7 failed')

board_init_3 = \
    [[0, 9, 1,    2, 0, 0,    0, 0, 4], \
     [8, 0, 0,    6, 0, 0,    1, 0, 0], \
     [0, 0, 4,    1, 5, 8,    0, 0, 0], \

     [4, 1, 5,    9, 6, 0,    2, 7, 8], \
     [9, 7, 6,    4, 8, 2,    5, 3, 1], \
     [3, 8, 2,    5, 1, 7,    6, 4, 9], \

     [0, 0, 0,    0, 0, 5,    0, 0, 0], \
     [0, 0, 0,    8, 0, 6,    4, 1, 0], \
     [0, 0, 0,    0, 0, 0,    0, 5, 0]]

board_object_3 = Board(board_init_3)

# print(board_object_3.board[3][5].possible_values)
board_object_3.unique_by(3, 5, 'row')
# print(board_object_3.board[3][5].possible_values)
test_unique_by_2 = \
    board_object_3.board[3][5].possible_values == 3
print('Test 8 passed' if test_unique_by_2 else 'Test 8 failed')

board_init_4 = \
    [[0, 4, 8,    6, 1, 5,    7, 2, 3], \
     [7, 0, 5,    0, 0, 0,    0, 0, 1], \
     [0, 0, 6,    0, 0, 0,    0, 0, 0], \

     [0, 0, 1,    0, 0, 0,    3, 8, 0], \
     [0, 8, 7,    0, 0, 9,    0, 6, 0], \
     [0, 0, 0,    1, 0, 0,    0, 0, 0], \

     [0, 2, 4,    3, 0, 1,    0, 7, 0], \
     [6, 0, 9,    0, 2, 0,    0, 0, 4], \
     [0, 0, 3,    4, 9, 0,    0, 0, 0]]

board_object_4 = Board(board_init_4)

# print(board_object_4.board[5][2].possible_values)
board_object_4.unique_by(5, 2, 'col')
# print(board_object_4.board[5][2].possible_values)
test_unique_by_3 = \
    board_object_4.board[5][2].possible_values == 2
print('Test 9 passed' if test_unique_by_3 else 'Test 9 failed')

# print(board_object_4.board[0][0].possible_values)
board_object_4.unique_by(0, 0, 'row')
# print(board_object_4.board[0][0].possible_values)
test_unique_by_4 = \
    board_object_4.board[0][0].possible_values == 9
print('Test 10 passed' if test_unique_by_4 else 'Test 10 failed')


################################ Testing run_game ##############################
board_init_5 = \
    [[9, 6, 4,    1, 8, 5,    2, 3, 7], \
     [2, 3, 5,    7, 9, 6,    0, 0, 1], \
     [0, 0, 7,    2, 3, 4,    9, 0, 6], \

     [0, 0, 0,    9, 0, 3,    0, 2, 8], \
     [7, 0, 8,    6, 5, 2,    0, 0, 3], \
     [0, 2, 0,    8, 0, 1,    0, 0, 5], \

     [0, 9, 2,    3, 0, 8,    5, 0, 4], \
     [0, 7, 0,    0, 0, 9,    0, 0, 2], \
     [0, 8, 0,    4, 2, 7,    0, 6, 9]]

board_init_5_result = \
    [[9, 6, 4,    1, 8, 5,    2, 3, 7], \
     [2, 3, 5,    7, 9, 6,    4, 8, 1], \
     [8, 1, 7,    2, 3, 4,    9, 5, 6], \

     [1, 5, 6,    9, 4, 3,    7, 2, 8], \
     [7, 4, 8,    6, 5, 2,    1, 9, 3], \
     [3, 2, 9,    8, 7, 1,    6, 4, 5], \

     [6, 9, 2,    3, 1, 8,    5, 7, 4], \
     [4, 7, 3,    5, 6, 9,    8, 1, 2], \
     [5, 8, 1,    4, 2, 7,    3, 6, 9]]

board_object_5 = Board(board_init_5)

# print(board_object_4.board[5][2].possible_values)
board_object_5.run_game()
print(board_object_5)
test_run_game_1 = \
    board_object_5.arrayfy() == board_init_5_result
print('Test 11 passed' if test_run_game_1 else 'Test 11 failed')
