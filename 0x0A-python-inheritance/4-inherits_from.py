#!/usr/bin/python3
"""
Module containing the function inherits_from
"""


def inherits_from(obj, a_class):
    """
    function that returns true if an object is
    directly or indirectly inherited from a-class
    """

    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class):
        return True
