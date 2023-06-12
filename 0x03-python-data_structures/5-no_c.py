#!/usr/bin/python3
"""function that removes all characters c and C from a string."""
def no_c(my_string):
    retval = [listvar for listvar in my_string if listvar != 'c' and listvar != 'C']
    return ("".join(retval))
