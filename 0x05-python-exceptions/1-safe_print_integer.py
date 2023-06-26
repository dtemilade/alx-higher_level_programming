#!/usr/bin/python3
"""prototype function that prints an integer with "{:d}".format()
Returns True if value has been correctly printed (it means the value is an integer)
Otherwise, returns False
"""



def safe_print_integer(value):
"""Handling Exceptions"""
try:
print("{:d}".format(value))
return (True)
except (TypeError, ValueError):
return (False)
