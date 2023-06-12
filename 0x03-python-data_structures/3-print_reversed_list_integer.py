#!/usr/bin/python3
"""function that prints all integers of a list, in reverse order"""
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list.reverse()
        for listvar in my_list:
            print("{:d}".format(listvar))
