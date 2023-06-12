#!/usr/bin/python3
"""function that replaces an element of a list at a specific position"""


def replace_in_list(my_list, idx, element):
    """idx is negative or out of range, return None"""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
        """Output the result"""
        return my_list
    else:
        return None
