#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for rows in matrix:
        for element in rows:
            print("{:d}".format(int(element)), end=" ")
        print()
