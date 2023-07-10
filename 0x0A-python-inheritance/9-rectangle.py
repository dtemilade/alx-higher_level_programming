#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The class; template to perform the task."""

    def __init__(self, width, height):
        """The method with parameters to perform the task."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """output with the result"""
        return self.__height * self.__width

    def __str__(self):
        """output with special method"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
