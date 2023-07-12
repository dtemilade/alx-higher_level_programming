#!/usr/bin/python3
""" function that returns a list of lists of integers
representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """conditional statement for the program"""
    if n <= 0:
        return []

    retval = [[1]]
    while len(retval) != n:
        j = retval[-1]
        i = [1]
        for k in range(len(j) - 1):
            i.append(j[k] + j[k + 1])
        i.append(1)
        retval.append(i)
    return retval
