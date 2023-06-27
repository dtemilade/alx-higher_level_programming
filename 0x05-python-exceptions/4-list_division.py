#!/usr/bin/python3
"""prototype function that divides element by element 2 lists.
Returns a new list (length = list_length) with all divisions
"""

def list_division(my_list_1, my_list_2, list_length):
    """introducing an array"""
    retval = []
    """introducing conditional statement with exception handling"""
    for tstval in range(0, list_length):
        try:
            div = my_list_1[tstval] / my_list_2[tstval]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            retval.append(div)
    return (retval)
