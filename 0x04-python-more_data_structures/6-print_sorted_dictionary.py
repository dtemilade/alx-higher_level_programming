#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    """function prototype conditional statement"""
    for t in list_ord:
        print("{}: {}".format(t, a_dictionary.get(t)))
