#!/usr/bin/python3
"""
This is '0-lookup' module.
Functions and Classes:
    def lookup(obj)
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    """
    return dir(obj)
