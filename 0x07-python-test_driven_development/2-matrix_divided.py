#!/usr/bin/python3

""" A matrix divisor
Divides all elements of a matrix by div
"""


def matrix_divided(matrix, div):
    """ Divivdes a matrix by div

    Args:
        matrix (list): list of ints/floats
        div (int): non zero number
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(item, list) for item in matrix) or not
            all(isinstance(item, (int, float)) for row in matrix
                for item in row)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    n_m = [[round((item / div), 2) for item in li] for li in matrix]
    return n_m
