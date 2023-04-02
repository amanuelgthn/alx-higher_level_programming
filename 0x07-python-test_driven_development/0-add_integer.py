#!/usr/bin/python3
"""
Module to add two integers or floats
floats are casted to integers
raise TypeError if type is other than int or floats
"""


def add_integer(a, b=98):
    """
    Function to add two integers or floats
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
