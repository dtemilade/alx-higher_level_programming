#!/usr/bin/python3
"""Creates a new type: class Square."""


class Square:
    """Define __init___ method for square."""

    def __init__(self, size=0):
        """Initialize a new square using instance method"""
        self.size = size

    @property
    def size(self):
        """Assigning current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """conditional statement for the method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returning the area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Introducing == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Introducing != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Introducing < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Introducing <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Introducing > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Introducing >= compmarison to a Square."""
        return self.area() >= other.area()
