#!/usr/bin/python3
"""Function find_peak that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""

    if not list_of_integers:
        return None

    retval = list_of_integers[0]

    for i in list_of_integers:
        if i > retval:
            retval = i

    return retval
