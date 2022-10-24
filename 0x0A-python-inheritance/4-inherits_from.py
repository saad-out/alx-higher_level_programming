#!/usr/bin/python3
"""
This is '4-inherits_from' module.
Functions and Classes:
    def inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """
    check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    """
    related = issubclass(obj.__class__, a_class)
    not_same_class = (obj.__class__ is not a_class)

    return (related and not_same_class)
