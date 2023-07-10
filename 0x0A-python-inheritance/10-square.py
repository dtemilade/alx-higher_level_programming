#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The class; template to perform the task."""

    def __init__(self, size):
        """The method with parameters to perform the task."""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
