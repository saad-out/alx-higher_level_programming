#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for l in matrix:
        new_matrix.append([x**2 for x in l])
    return new_matrix
