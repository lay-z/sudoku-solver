from sudoku import Sudoku

sudoku = Sudoku("tests/puzzle.csv")
print sudoku

# print sudoku.recursive_solve(0, 0)
#
# print sudoku
#
# sudoku.board = sudoku.board.astype(int)
#
# sudoku.board.to_csv("test.csv", index=False, header=False)
