# cell.py
# class definition for a cell on a sudoku board

value_range = range(1, 10)

class Cell:

    possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, value):
        self.setValue(value)

    def setValue(self, possible_values):

        if type(possible_values) is int:

            if possible_values in value_range:
                self.possible_values = possible_values;

            elif possible_values == 0:
                self.possible_values = value_range

            else:
                raise ValueError('trying to set cell to an invalid int %s' \
                    % possible_values)
        else:
            # possible_values is an array
            for possible_value in possible_values:
                if possible_value in value_range:
                    continue
                else:
                    raise ValueError('trying to set cell to an invalid array %s' \
                        % possible_values)

            self.possible_values = possible_values


    def getValue(self):

        if self.possible_values:
            return self.possible_values;

    def check(self, other):
        if type(self.possible_values) is int:
            raise ValueError('you cannot check against a set value')
        else:
            other_value = other.getValue()
            if type(other_value) is int:
                self.possible_values.remove(other_value)
