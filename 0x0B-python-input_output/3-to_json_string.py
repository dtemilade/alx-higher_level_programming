#!/usr/bin/python3
import json
"""function that returns the JSON representation of an object (string):"""


def to_json_string(my_obj):
    """dumps() function to return JSON string representation"""
    return json.dumps(my_obj)
