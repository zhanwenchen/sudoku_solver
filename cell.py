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
                try:
                    self.possible_values.remove(other_value)
                    # print('check(): removed %s from current cell. It is now %s. Other value is now %s'\
                    #     % (other_value, self.possible_values, other_value))

                except:
                    print('check(): current cell does not contain %s. It is %s. Other value is now %s'\
                        % (other_value, self.possible_values, other_value))
            # else:
            #     print('other contains an array %s' % (other.possible_values))
