#!/usr/bin/python3
"""
This is '1-my_list' module.
Functions and Classes:
    class MyList
"""


class MyList(list):
    """
    subclass that inherits from 'list' class
    """
    def print_sorted(self):
        """print sorted list in ascending order"""
        print(sorted(self))
