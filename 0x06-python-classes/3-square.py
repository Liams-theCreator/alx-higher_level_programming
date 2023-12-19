#!/usr/bin/python3

"""Class documentation"""


class Square:
    """Class documentation"""

    def __init__(self, size=0):
        """__init__ constructor method"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """method to return area of the instantiated square."""
        return self.__size * self.__size
