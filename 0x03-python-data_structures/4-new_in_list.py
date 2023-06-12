#!/usr/bin/python3
"""function that replaces an element in a list at a specific position
    without modifying the original list (like in C).
    """


def new_in_list(my_list, idx, element):
    """idx is negative or out of range, return original list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    retval = my_list.copy()
    retval[idx] = element
    return (retval)
