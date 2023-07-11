#!/usr/bin/python3
""" function that inserts a line of text to a file, after each line containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file."""
    retval = ""
    with open(filename) as r:
        for line in r:
            retval = retval + line
            if search_string in line:
                retval = retval + new_string
    """with statement used to properly closed the file after its suite finishes"""
    with open(filename, "w") as w:
        w.write(retval)
