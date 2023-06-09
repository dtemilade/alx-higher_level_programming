#!/usr/bin/python3

"""Executing the modules as scripts:
    by executing the module as the “main” file:
    """

if __name__ == "__main__":

    import sys

    """program conditional statement"""
    retval = len(sys.argv) - 1
    if retval == 0:
        print("0 arguments.")
    elif retval == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(retval))

        for testval in range(retval):
            print("{}: {}".format(testval + 1, sys.argv[testval + 1]))
