#!/usr/bin/python3
"""Creates a new type: class Square."""


class Square:
    """Define __init___ method for square."""

    def __init__(self, size=0):
        """Instantiate the square with private attribute: size
        Instantiation with optional as provided using conditional statement.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """Introduce Public instance method to return current area of the square."""

    def area(self):
        return (self.__size * self.__size)
