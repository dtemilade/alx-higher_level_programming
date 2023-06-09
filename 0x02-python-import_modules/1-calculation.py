#!/usr/bin/python3

"""Executing the modules as scripts:
by executing the module as the “main” file:
"""

if __name__ == "__main__":

    """importing the functions from the file"""
    from calculator_1 import add, sub, mul, div

    """defining values for variable a and b separately"""
    a = 10
    b = 5

    """Maths operations and their results"""
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
