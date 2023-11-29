#!/usr/bin/python3
import sys

"""
The N queens puzzle is the challenge of placing N non-attacking
    queens on an N×N chessboard. Write a program that
    solves the N queens problem.

"""


class QueensBoard:
    def __init__(self, size):
        """
        Initialize a QueensBoard object.

        Parameters:
            - size: The size of the chessboard.
        """
        self.size = size
        self.board = [-1] * size
        self.solutions = []

    def is_safe(self, row, col):
        """
        Check if placing a queen at a specific position is safe.

        Parameters:
            - row: The row of the chessboard.
            - col: The column of the chessboard.

        Returns:
            - True if placing a queen is safe, False otherwise.
        """
        for i in range(row):
            if self.board[i] == col or self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    def solve_nqueens_util(self, row):
        """
        Recursively find all solutions to the N-Queens problem.

        Parameters:
            - row: The current row being considered.
        """
        if row == self.size:
            r = self.solutions.append
            r([[i, self.board[i]] for i in range(self.size)])
            return

        for col in range(self.size):
            if self.is_safe(row, col):
                self.board[row] = col
                self.solve_nqueens_util(row + 1)

    def solve_nqueens(self):
        """
        Solve the N-Queens problem for the chessboard.

        Returns:
            - A list of solutions, where each solution is a
                list of pairs [row, col].
        """
        self.solutions = []
        self.solve_nqueens_util(0)
        return self.solutions


def main():
    """
    Main function to handle command-line arguments and print solutions.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        board = QueensBoard(N)
        solutions = board.solve_nqueens()

        for solution in solutions:
            print(solution)

    except ValueError:
        print("N must be a number")
        sys.exit(1)


if __name__ == "__main__":
    main()
