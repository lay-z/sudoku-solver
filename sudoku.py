import pandas as pd
from math import isnan
from numpy import NaN


def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return value


class Sudoku:
    """
    holds a representation of sudoku game
    """

    def __init__(self, file_name):
        self.board = pd.read_csv(file_name, header=None)

    def solve(self):
        """
        Wrapper function around recursive_solve
        :return: Value of recursive_solve
        """
        return self.recursive_solve(0, 0)

    def recursive_solve(self, row, column):
        """
        Function to recursively solve sudoku board,
        Will try every possible combination of digits, if able to succesfully place digit
        Will run recursive_solve on next column
        :param row: Row to try place digits at
        :param column: column to try place digits at
        :return: Boolean depending on if board was solved or not
        """

        val = False

        if self.board_complete():
            return True

        # if position already has figure
        if not isnan(self.board[column][row]):
            # Go to next row/column
            if column < 8:
                val = self.recursive_solve(row, column + 1)
            else:
                val = self.recursive_solve(row + 1, 0)
            if val:
                return True
        # for positions that don't have figure
        else:
            # try every value from 1-9
            for i in range(1, 10):
                # print "trying number: {0}, for row: {1}, and column: {2}".format(i, row, column)
                # if the digit can be placed, move to next one
                if self.place_digit(i, row, column):
                    if column < 8:
                        val = self.recursive_solve(row, column + 1)
                    else:
                        val = self.recursive_solve(row + 1, 0)

                    if val:
                        return True
                # print self.board
                # Clear the number
                self.board[column][row] = NaN

        # If not able to find number that solves board
        # Then board is not solvable
        return val

    def board_complete(self):
        """

        :return: Boolean value, will be true if board is complete, Will be false if board incomplete
        """
        return not self.board.isnull().values.any()

    def place_digit(self, number, row, column):
        """
        Tries to place digit into board.
        If it can successfully place digit then return true, else return false
        :param row: Integer row to place number into board (starts from 0)
        :param column: Integer column to place number into board (starts from 0)
        :param number: Integer to be placed into board
        :return: Boolean: returns true if able to successfully place digit else false
        """
        # print "trying number: {0}, in row: {1}, in column: {2}".format(number, row, column)
        # If space is empty
        if isnan(self.board[column][row]):
            # check for numbers in column
            if self.board.loc[row].isin([number]).any():
                return False

            # check for same numbers in column
            if self.board[column].isin([number]).any():
                return False

            # check for same numbers in quadrant
            upper_row = row // 3 * 3
            lower_row = ((row // 3 + 1) * 3) - 1
            upper_column = column // 3 * 3
            lower_column = ((column // 3 + 1) * 3) - 1
            quadrant = self.board.loc[upper_row: lower_row, upper_column: lower_column]
            if quadrant.isin([number]).any().any():
                return False

            # If all other checks pass then add number to board and carry on
            self.board[column][row] = number
            return True

        return False

    def write_to_file(self, filename):
        """
        Helper function to write board to csv file
        :param filename: file name to save csv file as
        :return: None
        """
        self.board.to_csv(filename, index=False, header=False)

    def __getitem__(self, item):
        return self.board[item]

    def __str__(self):
        representation = ""
        for index, row in self.board.iterrows():
            for row_index, value in row.iteritems():
                if isnan(value):
                    representation += " "
                else:
                    representation += "{0}".format(int(value))

                if not ((row_index + 1) % 3):
                    representation += "|"

            representation += "\n"

            if not ((index + 1) % 3):
                representation += ("-" * 3 + "+" + "-" * 3 + "+" + "-" * 3 + "+")
                representation += "\n"
        return representation
