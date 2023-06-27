#!/usr/bin/python3
"""function that executes a function safely
Returns the result of the function, Otherwise, returns None.
Incase of error, prints in stderr the error precede by Exception:
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
