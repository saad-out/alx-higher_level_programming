#!/usr/bin/python3
"""
This is '9-rectangle' module.
Functions and Classes:
    class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represent a rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """compute the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of a Rectangle object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
