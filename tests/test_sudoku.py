from unittest import TestCase
from sudoku import Sudoku

from pandas import read_csv
from numpy import array_equal


class TestSudoku(TestCase):
    def setUp(self):
        self.board = Sudoku('puzzle.csv')

    def test_place_digit_should_place_digit_in_right_place(self):
        # given
        number = 1
        row = 1
        column = 1

        # when
        result = self.board.place_digit(number, row, column)

        # then
        self.assertTrue(result)
        self.assertEqual(self.board[row][column], number)

    def test_place_digit_should_not_allow_placing_digit_when_digit_exists(self):
        # given
        number = 7
        row = 0
        column = 0

        # when
        result = self.board.place_digit(number, row, column)
        # then
        self.assertFalse(result)

    def test_place_digit_should_now_allow_placing_digit_when_same_digit_exists_in_row(self):
        # given
        number = 4
        row = 0
        column = 1

        # when
        result = self.board.place_digit(number, row, column)
        # then
        self.assertFalse(result)

    def test_place_digit_should_now_allow_placing_digit_when_same_digit_exists_in_column(self):
        # given
        number = 7
        row = 0
        column = 1

        # when
        result = self.board.place_digit(number, row, column)
        # then
        self.assertFalse(result)

    def test_place_digit_should_not_allow_placing_digit_when_same_digit_exists_in_quadrant(self):
        # given
        number = 4
        row = 1
        column = 2

        # when
        result = self.board.place_digit(number, row, column)
        # then
        self.assertFalse(result)
    
    def test_place_digit_should_allow_placing_digit_when_same_digit_exists_in_other_quadrants(self):
        # given
        number = 4
        row = 1
        column = 5

        # when
        result = self.board.place_digit(number, row, column)

        # then
        self.assertTrue(result)
        self.assertEqual(self.board[row][column], number)

    def test_recursive_solve(self):
        # when
        self.board.recursive_solve(0, 0)
        print self.board

    def test_solve_should_solve_sudoku_puzzle(self):
        # given
        solved = read_csv("puzzle_solution.csv", header=None)

        # when
        self.board.solve()

        # then
        self.assertTrue(array_equal(self.board.board, solved),
                        msg="expected:\n {0} \n\n received:\n {1}".format(solved, self.board.board))

