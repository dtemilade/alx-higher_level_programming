#!/usr/bin/python3
"""Prototype for name-printing function."""


def say_my_name(first_name, last_name=""):
    """Declaration and the required process as follows:"""
    if not isinstance(first_name, str):
        raise TypeError("first_name is always a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name is always a string")
    print("My name is {} {}".format(first_name, last_name))
