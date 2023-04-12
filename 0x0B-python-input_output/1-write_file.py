#!/usr/bin/python3
"""
Module containing the function write_file
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file and
    returns the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
