#!/usr/bin/python3
"""function that returns True
if the object is exactly an instance of the specified class ;
otherwise False.
"""


def is_same_class(obj, a_class):
    """The method to perform the task with conditional statement."""
    if type(obj) != a_class:
        return False
    return True
