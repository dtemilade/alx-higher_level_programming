#!/usr/bin/python3
"""function that executes a function safely
Returns the result of the function, Otherwise, returns None
"""

import sys


def safe_function(fct, *args):
    """Handling Exceptions"""
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
