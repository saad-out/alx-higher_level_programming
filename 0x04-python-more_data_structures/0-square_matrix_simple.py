#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    if matrix:
        for l in matrix:
            new_list = [x**2 for x in l]
            new_matrix.append(new_list)

    return new_matrix
