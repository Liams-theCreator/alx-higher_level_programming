#!/usr/bin/python3
"""
    Task 1 - Mandatory
"""


class Rectangle:
    """
        Real definition of a rectangle
    """

    def __init__(self, width=0, height=0):
        """ Method - Initialize.
        Args:
            width (int): Width of the Rectangle
            height (int): Height of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            returns width
        """
        return self.__width

    @property
    def height(self):
        """
            returns height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
            sets width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
            sets height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
