#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print to stdout USING with statement.
    To properly closed the file after its suite finishes
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
