#!/usr/bin/python3
"""
to_json_string
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)
    Args:
    my_obj (str): object to return JSON representation of
    """
    return json.dumps(my_obj)
