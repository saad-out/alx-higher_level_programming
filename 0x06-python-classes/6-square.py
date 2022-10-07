#!/usr/bin/python3
"""module containing square class"""


class Square:
    """representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple) or (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position[0] = value[0]
            self.__position[1] = value[1]

    def area(self):
        """return the square area"""

        return (self.__size)**2

    def my_print(self):
        """" print square using '#' """

        for i in range(0, self.__position[1]):
            print("")

        if self.__size == 0:
            print("")
            return
        for j in range(0, self.__size):
            for sp in range(0, self.__position[0]):
                print(" ", end="")
            for i in range(0, self.__size):
                print("#", end="")
            print("")
