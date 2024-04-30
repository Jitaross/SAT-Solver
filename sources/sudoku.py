"""
This module will transform a sudoku problem into a SAT problem.
"""


def transform_sudoku_to_sat(sudoku):
    clauses = []

    # Each cell contains at least one number
    for i in range(9):
        for j in range(9):
            clauses.append([81 * i + 9 * j + k + 1 for k in range(9)])

    # Each cell contains at most one number
    for i in range(9):
        for j in range(9):
            for x in range(9):
                for y in range(x + 1, 9):
                    clauses.append([-(81 * i + 9 * j + x + 1), -(81 * i + 9 * j + y + 1)])

    # Each number appears at most once in each row
    for i in range(9):
        for k in range(9):
            for j in range(9):
                for l in range(j + 1, 9):
                    clauses.append([-(81 * i + 9 * j + k + 1), -(81 * i + 9 * l + k + 1)])

    # Each number appears at most once in each column
    for j in range(9):
        for k in range(9):
            for i in range(9):
                for l in range(i + 1, 9):
                    clauses.append([-(81 * i + 9 * j + k + 1), -(81 * l + 9 * j + k + 1)])

    # Each number appears at most once in each 3x3 square
    for k in range(9):
        for a in range(3):
            for b in range(3):
                cells = []
                for u in range(3):
                    for v in range(3):
                        cells.append(81 * (3 * a + u) + 9 * (3 * b + v) + k + 1)
                for x in range(9):
                    for y in range(x + 1, 9):
                        clauses.append([-cells[x], -cells[y]])

    # If a cell is filled, it contains the correct number
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                clauses.append([81 * i + 9 * j + sudoku[i][j]])

    with open("../resources/sudoku_c.cnf", "w") as file:
        file.writelines([f"{' '.join([str(lit) for lit in clause])}\n" for clause in clauses])

    return clauses


if __name__ == "__main__":
    sudoku_list = [
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [1, 5, 8, 0, 0, 0, 0, 3, 0],
        [3, 4, 0, 1, 6, 0, 9, 0, 2],
        [0, 0, 9, 2, 0, 8, 1, 7, 5],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 3, 5, 6, 0, 1, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 3, 9, 4],
        [5, 1, 3, 4, 8, 0, 0, 0, 7],
        [6, 9, 0, 7, 5, 2, 0, 0, 3]
    ]
    sat_problem = transform_sudoku_to_sat(sudoku_list)
    print(f"sat_problem : {sat_problem}\nnumber of clauses : {len(sat_problem)}")
