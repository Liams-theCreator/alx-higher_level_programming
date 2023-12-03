#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    idx = 0
    for rows in matrix:
        for idx, elements in enumerate(rows):
            print("{:d}".format(elements), end=" ")
    print()
