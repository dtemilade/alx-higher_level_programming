#!/usr/bin/python3
"""function that deletes the item at a specific position in a list."""
def delete_at(my_list=[], idx=0):
    """idx is negative or out of range, return original list"""
    if idx >= 0 and idx < len(my_list):
        """output the result"""
        del my_list[idx]
        return (my_list)
