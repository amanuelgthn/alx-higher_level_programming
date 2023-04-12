#!/usr/bin/python3
"""
Import module JSON
"""


import json
"""
Module containing the function save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """
    function that writes an object to a text file,using a JSON representation
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
