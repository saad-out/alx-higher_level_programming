#!/usr/bin/python3
"""
This is '3-is_kind_of_class' module.
Functions and Classes:
    def is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """
    checks whether an object is an instance of a class (exact or inherited)
    or not
    """
    return isinstance(obj, a_class)
