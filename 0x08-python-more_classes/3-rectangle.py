#!/usr/bin/python3
"""
    Task 2 - Mandatory
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

    def area(self):
        """
            Calculates and returns area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Calculates and returns perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * self.__width + 2 * self.__height

    def __str__(self):
        p_rectangle = ""
        count = 1
        if self.__width == 0 or self.__height == 0:
            return p_rectangle
        else:
            for i in range(self.__height):
                p_rectangle += "#" * self.__width
                if count != self.__height:
                    p_rectangle += "\n"
                count += 1
            return p_rectangle
