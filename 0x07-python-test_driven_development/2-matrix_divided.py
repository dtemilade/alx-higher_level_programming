#!/usr/bin/python3
"""Prototype for matrix division function."""


def matrix_divided(matrix, div):
    """Declaration and the required process as follows:"""
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(k, int) or isinstance(k, float))
                for k in [num for row in matrix for num in row])):
        raise TypeError("matrix is always a matrix (list of lists) of "
                "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix has the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div is always a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
