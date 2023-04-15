#!/usr/bin/python3
"""
MOdule that contains add_attribute function
"""


def add_attribute(obj, attr, value):
    if hasattr(obj, "__dict__"):
        setattr(obj,attr,value)
        return
    raise TypeError("can't add new attribute")
