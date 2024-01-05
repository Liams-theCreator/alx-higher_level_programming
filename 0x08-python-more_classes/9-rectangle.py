#!/usr/bin/python3
"""
    Task 9 - Mandatory
"""


class Rectangle:
    """
        Real definition of a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method - Initialize.
        Args:
            width (int): Width of the Rectangle
            height (int): Height of the Rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                p_rectangle += str(self.print_symbol) * self.__width
                if count != self.__height:
                    p_rectangle += "\n"
                count += 1
            return p_rectangle

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
