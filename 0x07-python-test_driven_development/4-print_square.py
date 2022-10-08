#!/usr/bin/python3
"""
This is '4-print_square' module.
Functions:
    print_square(size)
"""


def print_square(size):
    """
    print square with the '#' character

    args:
        size (int): size length of square
    return:
        None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print()
