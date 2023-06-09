#!/usr/bin/python3

"""declaring Python functions prototype"""
def magic_calculation(a, b):

    """importing operations function from the functions"""
    from magic_calculation_102 import add, sub

    """program conditional statement"""
    if a < b:
        c = add(a, b)
        for cons_var in range(4, 6):
            c = add(c, cons_var)
            return c
        else:
            return sub(a, b)
