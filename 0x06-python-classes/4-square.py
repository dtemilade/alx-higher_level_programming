#!/usr/bin/python3
"""Creates a new type: class Square."""


class Square:
    """Define __init___ method for square."""

    def __init__(self, size=0):
        """Instantiate the square with private attribute: size
        Instantiation with optional as provided using conditional statement.
        """
        self.size = size

    @property
    def size(self):
        """return current size of the square using return"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Conditional Statement for the prototype function
        Get integer otherwise raise a TypeError exception with the message
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """Introduce Public instance method to return current area of the square."""

    def area(self):
        return (self.__size * self.__size)
