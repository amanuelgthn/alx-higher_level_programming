#!/usr/bin/python3
"""
Module containing the function inherits_from
"""


def inherits_from(obj, a_class):
    """
    function that returns true if an object is
    directly or indirectly inherited from a-class
    """
    
    return (issubclass(obj, a_class)
