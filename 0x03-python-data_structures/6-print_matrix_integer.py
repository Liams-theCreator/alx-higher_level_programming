#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    idx = 0
    for rows in matrix:
        for idx, element in enumerate(rows):
            if idx != 0:
                print(" ", end="")
            print("{:d}".format(element), end="")
            idx += 1
        print()
