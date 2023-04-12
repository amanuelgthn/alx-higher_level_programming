#!/usr/bin/python3
"""
Import module JSON
"""

import json
"""
Module containing function from_json_string(my_str)
"""


def from_json_string(my_str):
    """
    function that returns an object(python data structure)
    represented by a JSON string
    """
    return json.dumps(my_str)
