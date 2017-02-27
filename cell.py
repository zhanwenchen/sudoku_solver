# cell.py
# class definition for a cell on a sudoku board



class Cell:

    def __init__(self):
        self.possible_values = range(1, 10)

    def __init__(self, possible_values):

        if possible_values == 0:
            self.possible_values = range(1, 10)
        elif possible_values in range(1, 10):
            self.possible_values = possible_values
        else:
            raise ValueError('trying to set cell to an invalid int %s' \
                % possible_values)

    # check current cell against another and remove the other value from the
    # possible values of current cell if the other cell is that int.
    def check(self, other):
        # print('in check(self = %s, other = %s)' % (self, other))
        if type(self.possible_values) is int:
            raise ValueError('current_cell is an int')
        else:
            other_value = other.possible_values
            if type(other_value) is int:
                if other_value in self.possible_values:
                    self.possible_values.remove(other_value)
                    if len(self.possible_values) == 1:
                        self.possible_values = self.possible_values[0]
                        return
                return False
            else:
                # if the other cell intersects with current cell
                if not set(self.possible_values).isdisjoint(other_value):
                    return True
                # print('other contains an array %s' % (other.possible_values))
