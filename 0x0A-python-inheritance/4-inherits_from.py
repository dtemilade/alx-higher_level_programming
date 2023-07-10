#!/usr/bin/python3
"""function that returns True if the object is an instance of a class
inherited (directly or indirectly) from the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """The method to perform the task with conditional statement."""
    if issubclass(type(obj), a_class) and type(obj) == a_class:
        return False
    return True
