#!/usr/bin/python3
"""
MOdule that contains add_attribute function
"""


def add_attribute(obj, attr, value):
    """
    function to add an atrribute if possible
    and raise TypeError if not possible
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
        return
    raise TypeError("can't add new attribute")
