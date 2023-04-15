#!/usr/bin/python3
"""
Module containing Class MyInt
"""


class MyInt(int):
    """
    MyInt class
    """

    def _eq__(self, other):
        return self != other
    
    def __ne__(self, other):
        return self == other