#!/usr/bin/python3
"""Prototype for an integer addition function."""


def add_integer(a, b=98):
    """Declaration and the required process as follows:"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a is always an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b is always an integer")
    return (int(a) + int(b))
