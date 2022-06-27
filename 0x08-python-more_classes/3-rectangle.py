#!/usr/bin/python3
"""
A Rectangle Class with the private instance attributes width, height
and public methods
"""


class Rectangle():
    """
    A Rectangle Class with the private instance attributes width and height
    """

    def __init__(self, width=0, height=0):
        """
        Constructor of the class Rectangle
          Args:
            - width (default = 0): int
            - heigth (default = 0): int
        """
        self.height = height
        self.width = width

    def area(self):
        """Calculate the area of a Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Get the perimeter of a Rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Function to print a Square with #
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        final = ['#' * self.__width for line in range(self.__height)]

        return '\n'.join(final)

    @property
    def width(self):
        """Getter of the property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Getter of the property value
          Args:
            - value: int
        """

