#!/usr/bin/python3
"""
This is '101-locked_class' module
Classes:
    LockedClass()
"""


class LockedClass():
    """
    prevent user from creating instances unless it's 'first_name'
    """
    __slots__ = ['first_name']
