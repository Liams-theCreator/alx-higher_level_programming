#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    newset = [[i * i for i in rows] for rows in matrix]
    return newset
