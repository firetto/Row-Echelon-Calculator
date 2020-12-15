"""
Row Echelon Calculator
Anatoly Zavyalov
"""


from typing import List, Tuple


def row_echelon(matrix: List[List[float]]) -> List[List[float]]:
    """
    Mutate matrix by putting it into row echelon form.

    Preconditions:
     - len(matrix) > 0
     - all(len(row) > 0 for row in matrix)
     - sum([1 for i in range(1, len(matrix)) if len(matrix[i]) != len(matrix[0])]) == 0
    """

    # Highest row not yet eliminated
    row = 0

    # Current column that you are looking at
    column = 0

    while column < len(matrix[0]):

        # ACCUMULATOR: Rows with a nonzero entry at column.
        nonzero_rows = []

        for i in range(row, len(matrix)):
            if matrix[i][column] != 0:
                nonzero_rows.append(i)

        for i in range(1, len(nonzero_rows)):
            shear_rows(matrix, nonzero_rows[i], nonzero_rows[0],
                       - matrix[nonzero_rows[i]][column] / matrix[nonzero_rows[0]][column])

        if len(nonzero_rows) > 0:
            # matrix[nonzero_rows[0]] = scale_row(matrix[nonzero_rows[0]], 1 / matrix[nonzero_rows[0]][column])

            swap_rows(matrix, (nonzero_rows[0], row))
            row += 1

        column += 1

    return matrix


def swap_rows(matrix: List[List[float]], rows: Tuple[int, int]) -> List[List[float]]:
    """
    Mutate matrix by swapping rows[0] and rows[1].

    Preconditions:
     - len(matrix) > 0
     - all(len(row) > 0 for row in matrix)
     - sum([1 for i in range(1, len(matrix)) if len(matrix[i]) != len(matrix[0])]) == 0
     - all([0 <= i < len(matrix) for i in rows])
    """

    temp = matrix[rows[0]]
    matrix[rows[0]] = matrix[rows[1]]
    matrix[rows[1]] = temp
    return matrix


def scale_row(row: List[float], scalar: float) -> List[float]:
    """
    Return the row scaled by scalar.
    """

    return [scalar * el for el in row]


def add_rows(row1: List[float], row2: List[float]) -> List[float]:
    """
    Return the sum of the rows by adding the corresponding elements of each row.

    Preconditions:
     - len(row1) == len(row2)
    """
    return [row1[i] + row2[i] for i in range(len(row1))]


def shear_rows(matrix: List[List[float]], target: int,
               by: int, scalar: float) -> List[List[float]]:
    """
    Mutate matrix by adding "scalar * by" to target row.
    """
    matrix[target] = add_rows(matrix[target], scale_row(matrix[by], scalar))
    return matrix
