"""
This module will transform the sudoku problem into a SAT problem.
"""


def transform_sudoku_to_sat(sudoku):
    """
    This function transforms a given Sudoku problem into a SAT problem.

    The function iterates over each cell in the Sudoku grid. If a cell already contains a number (i.e., it's not 0),
    it creates a clause representing that cell's value. It then creates clauses for each cell that could potentially
    contain a number, representing the constraints of the Sudoku game. These constraints include:
    - Each cell in a row must contain a unique number.
    - Each cell in a column must contain a unique number.
    - Each cell in a 3x3 grid must contain a unique number.

    The function returns a list of clauses that represent the SAT problem equivalent of the given Sudoku problem.

    :param sudoku: A 9x9 list of lists representing the Sudoku problem. Each inner list represents a row in the Sudoku grid.
                   Each cell in the grid is represented by an integer between 0 and 9, where 0 represents an empty cell.
    :return: A list of lists representing the SAT problem. Each inner list is a clause, and each integer in the clause
             represents a literal.
    """
    clauses = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                # Create a clause for each cell that already contains a number
                clauses.append([sudoku[i][j] + 9 * i + 81 * j])
    for i in range(9):
        for j in range(9):
            for k in range(9):
                # Create a clause for each cell that could potentially contain a number
                clauses.append([-(k + 1 + 9 * i + 81 * j) for k in range(9) if k + 1 != sudoku[i][j]])
    for i in range(9):
        for k in range(9):
            # Create a clause for each row in the Sudoku grid
            clauses.append([k + 1 + 9 * i + 81 * j for j in range(9)])
    for j in range(9):
        for k in range(9):
            # Create a clause for each column in the Sudoku grid
            clauses.append([k + 1 + 9 * i + 81 * j for i in range(9)])
    for i in range(3):
        for j in range(3):
            for k in range(9):
                # Create a clause for each 3x3 grid in the Sudoku grid
                clauses.append(
                        [k + 1 + 9 * a + 81 * b for a in range(3 * i, 3 * i + 3) for b in range(3 * j, 3 * j + 3)])
    return clauses


if __name__ == "__main__":
    sudoku_list = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 6, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]
