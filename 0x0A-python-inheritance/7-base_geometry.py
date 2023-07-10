#!/usr/bin/python3
"""a class BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """method that raises an Exception with the message"""

    def area(self):
        """output the Exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method  that validates value; be it not integer or <= 0"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
