#!/usr/bin/python3
"""prototype function that raises a name exception with a message
Returns True if value has been correctly printed (it means the value is an integer)
Otherwise, returns False and prints in stderr the error precede by Exception
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
