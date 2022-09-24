#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        space = False
        for column in row:
            if space:
                print(" ", end="")
            else:
                space = True
            print("{:d}".format(column), end="")
        print("")
