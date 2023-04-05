#!/usr/bin/python3
"""
This is  the LockedClass Module containing LockedClass class to preventing
the user from dynamically creating new instance attributes except for
first_name
"""


class LockedClass:
    """
    Locked class
    """
    __slots__ = ['first_name']
