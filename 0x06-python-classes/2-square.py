#!/usr/bin/python3
"""Class Square with private instance size"""


class Square:
    """Class Square with private instance size"""
    def __init__(self, size=0):
        try:
            num = int(size)
            if num < 0:
                raise Exception("size must be >= 0")
            else:
                 self.__size = size
        except TypeError:
            print("size must be an integer")
