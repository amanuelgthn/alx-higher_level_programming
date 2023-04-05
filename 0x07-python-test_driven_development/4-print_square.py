#!/usr/bin/python3
"""
This is a module that prints a square with the character #
"""


def print_square(size):
    """
    Function to print a square with the cahracter #
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print()
