#!/usr/bin/python3


def number_keys(a_dictionary):
    """variable parameter"""
    retval = 0
    list_keys = list(a_dictionary.keys())

    """function prototype conditional statement"""
    for t in list_keys:
        retval = retval + 1

    return (retval)
