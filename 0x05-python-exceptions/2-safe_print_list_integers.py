#!/usr/bin/python3
"""Print the first x elements of a list that are integers.
Returns the real number of integers printed
"""



def safe_print_list_integers(my_list=[], x=0):
    """introducing variable"""
    retval = 0

    for tstval in range(0, x):
        """Handling Exceptions"""
        try:
            print("{:d}".format(my_list[tstval]), end="")
            retval += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (retval)
