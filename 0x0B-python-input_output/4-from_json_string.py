#!/usr/bin/python3
import json
""" function that returns an object (Python data structure)
represented by a JSON string:
"""


def from_json_string(my_str):
    """loads() function to decode the object, then return"""
    return json.loads(my_str)
