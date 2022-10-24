#!/usr/bin/python3
"""
This is '7-base_geometry' module.
Functions and Classes:
    class BaseGeometry
"""


class BaseGeometry():
    """Geometry class"""
    def area(self):
        """raise an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate that value is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
