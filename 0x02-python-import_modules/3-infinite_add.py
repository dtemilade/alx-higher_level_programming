#!/usr/bin/python3

"""Executing the modules as scripts:
    by executing the module as the “main” file:
    """

if __name__ == "__main__":

    import sys

    """initializing value for output variable"""
    retval = 0

    """program conditional statement"""
    for testval in range(len(sys.argv) - 1):
        """update output variable and casting arguments into integers"""
        retval = retval + int(sys.argv[testval + 1])

    """printing the result"""
    print(retval)
