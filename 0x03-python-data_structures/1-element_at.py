#!/usr/bin/python3
"""function that retrieves an element from a list like in C"""
def element_at(my_list, idx):
    """idx is negative or out of range, return None"""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    """Output the result"""
    return (my_list[idx])
