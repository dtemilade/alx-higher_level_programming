#!/usr/bin/python3
"""prototype function that raises a name exception with a message
Returns True if value has been correctly printed else False
"""

import sys


def safe_print_integer_err(value):
    """Handling Exceptions"""
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
