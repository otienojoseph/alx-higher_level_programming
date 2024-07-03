#!/usr/bin/python3
"""Matrix Divider"""


def matrix_divided(matrix, div):
    """
        Function that divides all elements of a matrix

        Args:
            matrix - same size list of integers or floats
            div - number that can't be 0

        Returns - new matrix where all elements are divided with div

        Raises:
            TypeError:
                - If matrix is not of type int or float
                - Matrix rows are not the same size
                - div is not an int or float
            ZeroDivisionError:
                - div is 0
    """
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    
    result_matrix = []
    for list in range(len(matrix)):
        res = []
        for number in range(len(matrix[list])):
            if not isinstance(matrix[list][number], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            try:
                result = round(matrix[list][number] / div, 2)
                res.append(result)
            except ZeroDivisionError:
                raise ZeroDivisionError("division by zero")

        result_matrix.append(res)
    return result_matrix
