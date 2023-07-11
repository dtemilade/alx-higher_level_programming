#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """File mode 'w' for only writing to text file,
    with statement used to properly closed the file after its suite finishes
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
