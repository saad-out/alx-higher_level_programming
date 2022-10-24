#!/usr/bin/python3
"""
This is '2-is_same_class' module.
Functions and Classes:
    def is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """
    checks whether an object is an instance of a class or not
    """
    return obj.__class__ is a_class
