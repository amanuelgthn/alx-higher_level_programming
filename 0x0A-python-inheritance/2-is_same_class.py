#!/usr/bin/python3
"""
Module to containing the function is_same_class
"""


def is_same_class(obj, a_class):
    """
    function that returns true if obj is of a_class
    """
    return type(obj) == a_class
