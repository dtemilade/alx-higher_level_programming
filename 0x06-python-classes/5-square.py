#!/usr/bin/python3
"""Creates a new type: class Square."""


class Square:
    """Define __init___ method for square."""

    def __init__(self, size):
        """Instantiate the square with private attribute: size
        Instantiation with optional as provided using conditional statement.
        """
        self.size = size

    @property
    def size(self):
        """Assigning current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return current size of the square using return"""
        return (self.__size * self.__size)
    """Introduce method that print square with the character #"""

    def my_print(self):
        """conditional statement for the method"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
