#!/usr/bin/python3
"""function that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    retval = my_list[0]
    for listvar in range(len(my_list)):
        if my_list[listvar] > retval:
            retval = my_list[listvar]
    return (retval)
