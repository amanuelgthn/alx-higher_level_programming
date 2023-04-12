#!/usr/bin/python3
import json
"""
Module containing function to_json_string function
"""


def to_json_string(my_obj):
    """
    function that returns the JSON
    representation of an object(string)"""
    return json.dumps(my_obj)