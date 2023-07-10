#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """The class; template to perform the task."""

    def __eq__(self, value):
        """The method with parameters to perform the task."""
        return self.real != value

    def __ne__(self, value):
        """The method with parameters to perform the task."""
        return self.real == value
