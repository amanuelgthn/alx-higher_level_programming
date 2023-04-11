#!/usr/bin/python3
"""
This is a module containing a function that returns
the list of available attributes and methods of an object
"""


def lookup(obj):
    return dir(obj)