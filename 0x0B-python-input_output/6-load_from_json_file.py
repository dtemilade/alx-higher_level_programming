#!/usr/bin/python3
import json
"""function that creates an Object from a “JSON file”:"""


def load_from_json_file(filename):
    """load() function to decode the object
    with statement used to properly closed the file after its suite finishes
    """
    with open(filename) as f:
        return json.load(f)
