#!/usr/bin/python3
"""Prototype for square-printing function."""


def print_square(size):
    """Declaration and the required process as follows:"""
    if not isinstance(size, int):
        raise TypeError("size is always an integer")
    if size < 0:
        raise ValueError("size is always >= 0")
    for x in range(size):
        [print("#", end="") for i in range(size)]
        print("")
