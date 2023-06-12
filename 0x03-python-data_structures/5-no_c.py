#!/usr/bin/python3
"""function that removes all characters c and C from a string."""


def no_c(my_string):
    retval = [k for k in my_string if k != 'c' and k != 'C']
    return ("".join(retval))
