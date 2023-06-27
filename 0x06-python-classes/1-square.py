#!/usr/bin/python3
"""Creates a new type: class Square."""


class Square:
    """Define __init___ method for square."""

    def __init__(self, size):
        """Instantiate the square with private attribute: size
        As the size of a square is crucial for a square 
        """
        self.__size = size
