#!/usr/bin/python3
"""
Module containing append_write function
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text
    and returns the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
