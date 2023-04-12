#!/usr/bin/python3
"""
Module containing read_file function
"""


def read_file(filename=""):
    """
    function to read a file
    """

    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end="")
