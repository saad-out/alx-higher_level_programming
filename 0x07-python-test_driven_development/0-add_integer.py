#!/usr/bin/python3
"""
This is '0-add_integer' module.
Functions:
    add_ineger(a, b=98)
"""


def add_integer(a, b=98):
    """
    compute the sum of two integers and return it.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
