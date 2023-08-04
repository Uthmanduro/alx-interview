#!/usr/bin/python3
"""solves the N queens problem"""
import sys


def nqueens(n):
    """solves the N queens problem"""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    col = set()
    pos_diag = set()
    neg_diag = set()

    response = []
    board = [["0"] * n for _ in range(n)]

    def backtracking_algo(row=0):
        """backtracking algo"""
        if row == n:
            coord = [[row, column.index("Q")] for row, column in
                     enumerate(board)]
            response.append(coord)
            return

        for col_num in range(n):
            if col_num in col or (row + col_num) in pos_diag\
                    or (row - col_num) in neg_diag:
                continue

            col.add(col_num)
            pos_diag.add(row + col_num)
            neg_diag.add(row - col_num)
            board[row][col_num] = "Q"

            backtracking_algo(row + 1)

            col.remove(col_num)
            pos_diag.remove(row + col_num)
            neg_diag.remove(row - col_num)
            board[row][col_num] = "0"

    backtracking_algo()
    return response


try:
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    result = nqueens(int(sys.argv[1]))
    for i in result:
        print(i)
except ValueError:
    print("N must be a number")
    sys.exit(1)
