#!/usr/bin/python3
"""function that finds all multiples of 2 in a list."""
def divisible_by_2(my_list=[]):
    retval = []
    for listvar in range(len(my_list)):
        if my_list[listvar] % 2 == 0:
            retval.append(True)
            else:
                retval.append(False)

            return (retval)
