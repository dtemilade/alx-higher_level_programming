#!/usr/bin/python3
"""function prototype"""


def multiply_by_2(a_dictionary):
    retval = a_dictionary.copy()
    list_keys = list(retval.keys())

    """function prototype conditional statement"""
    for t in list_keys:
        retval[t] *= 2

    return (retval)
