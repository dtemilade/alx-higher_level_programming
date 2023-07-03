#!/usr/bin/python3
"""prototype that define a Rectangle based on main file"""


class Rectangle:
    """Declaration of the class and the required process for the program:"""

    def __init__(self, width=0, height=0):
        """Define the rectangle and its parameters"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Declare the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Declare the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Display result for area of the Rectangle."""
        return (self.__height * self.__width)

    def perimeter(self):
        """Display result for perimeter of the Rectangle."""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """Display result for Rectangle with the # character."""
        if self.__height == 0 or self.__width == 0:
            return ("")

        retval = []
        for x in range(self.__height):
            [retval.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                retval.append("\n")
                return ("".join(retval))

    def __repr__(self):
        """Display result for string representation of the Rectangle."""
        retval = "Rectangle(" + str(self.__width)
        retval += ", " + str(self.__height) + ")"
        return (retval)
