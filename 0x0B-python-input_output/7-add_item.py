#!/usr/bin/python3
import sys
"""script that adds all arguments to a Python list, then save them to a file:
Using functions as specified.
"""

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    """backslash used to indicate continuation of line"""
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    """process to create, If the file doesn’t exist"""

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
