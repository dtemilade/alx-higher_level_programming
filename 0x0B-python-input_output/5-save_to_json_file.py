#!/usr/bin/python3
import json
"""function that writes an Object to a text file,
    using a JSON representation:
    """


def save_to_json_file(my_obj, filename):
    """ dump() function to serializes the object to a text file
    with statement used to properly closed the file after its suite finishes
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
