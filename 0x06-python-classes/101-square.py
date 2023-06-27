#!/usr/bin/python3
"""Creates a new type: class Square."""


class Square:
    """Define __init___ method for square."""

    def __init__(self, size=0, position=(0, 0)):
        """declaring size and position to Initialize new square."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Assigning current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """conditional statement for the method"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Introduce method to return current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Introduce method that print 	square with the character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for c in range(0, self.__position[1])]
        for c in range(0, self.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            print("")

    def __str__(self):
        """Introducing print() representation of a Square."""
        if self.__size != 0:
            [print("") for x in range(0, self.__position[1])]
        for c in range(0, self.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            if c != self.__size - 1:
                print("")
        return ("")
