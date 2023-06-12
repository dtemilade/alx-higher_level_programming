#!/usr/bin/python3
"""function that prints all integers of a list."""
def print_list_integer(my_list=[]):
    """conditional statement for the function"""
    for listvar in range(len(my_list)):
        print("{:d}".format(my_list[listvar]))
