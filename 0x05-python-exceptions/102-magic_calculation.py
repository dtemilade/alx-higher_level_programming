#!/usr/bin/python3
"""Python function def magic_calculation(a, b):
that does exactly the same as the following Python bytecode:
"""

def magic_calculation(a, b):
    """introducing variable parameter"""
    retval = 0

    """introducing conditional statement with exception handling"""
    for tstval in range(1, 3):
        try:
            if tstval > a:
                raise Exception('Too far')
            else:
                retval += a ** b / i
        except:
            retval = b + a
            break
    return (retval)
