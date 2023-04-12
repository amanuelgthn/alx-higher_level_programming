#!/usr/bin/python3
"""
Import Module JSON
"""


import json
"""
Module containing load_from_json_file function
"""


def load_from_json_file(filename):
    """
    function that creates object from json file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
