#!/usr/bin/python3
""" function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """File mode 'a' opens the file for appending
    with statement used to properly closed the file after its suite finishes
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
