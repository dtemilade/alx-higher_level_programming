#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
new_matrix = matrix.copy()

"""function prototype conditional statement"""
for t in range(len(matrix)):
new_matrix[t] = list(map(lambda x: x**2, matrix[t]))

return (new_matrix)
