#!/usr/bin/python3
"""
Module Containing function class_to_json
"""


def class_to_json(obj):
    """
    function that returns the dictionary description
    with simple data structure
    """
    return vars(obj)
