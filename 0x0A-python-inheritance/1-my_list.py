#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """The class; template to perform the task."""

    def print_sorted(self):
        """method that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
