#!/usr/bin/python3
"""Function find_peak that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""

    if list_of_integers is None or list_of_integers == []:
        return None
    x = 0
    y = len(list_of_integers)
    retval = ((y - x) // 2) + x
    retval = int(retval)
    if y == 1:
        return list_of_integers[0]
    if y == 2:
        return max(list_of_integers)
    if list_of_integers[retval] >= list_of_integers[retval - 1] and\
            list_of_integers[retval] >= list_of_integers[retval + 1]:
        return list_of_integers[retval]
    if retval > 0 and list_of_integers[retval] < list_of_integers[retval + 1]:
        return find_peak(list_of_integers[retval:])
    if retval > 0 and list_of_integers[retval] < list_of_integers[retval - 1]:
        return find_peak(list_of_integers[:retval])
