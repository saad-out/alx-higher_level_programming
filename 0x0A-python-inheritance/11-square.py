#!/usr/bin/python3
"""
This is '11-square' module.
Functions and Classes:
    class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent a square"""
    def __init__(self, size):
        self.intger_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """string representation of a Square object"""
        return "[Square] {}/{}".format(self.__size, self.__size)
