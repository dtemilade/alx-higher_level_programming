#!/usr/bin/python3

"""Executing the modules as scripts:
    by executing the module as the “main” file:
    """

if __name__ == "__main__":
    from add_0 import add

    """defining values for variable a and b"""
    a = 1
    b = 2

    """program output as thus:"""
    print("{} + {} = {}".format(a, b, add(a, b)))
