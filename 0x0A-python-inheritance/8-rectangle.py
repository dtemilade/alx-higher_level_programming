#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The class; template to perform the task."""

    def __init__(self, width, height):
        """The method with parameters to perform the task."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
