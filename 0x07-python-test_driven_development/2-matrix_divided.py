#!/usr/bin/pyth0n3
"""
this module contains a function that divides elements in a matrix
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix
    Args:
        matrix: lists of lists of integers or floats
        div: a number to divide by the matrix
    Raises:
        TypeError: matrix must be list of lists with integers or floats
        ZeroDivisionError: div must be greater than 0
    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(error_msg)

    length = 0

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError(error_msg)

        if length != 0 and len(i) != length:
            raise TypeError("Each row of the matrix must have the same size")

        for j in i:
            if not type(j) in (int, float):
                raise TypeError(error_msg)

        length = len(i)

    nm = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return nm
