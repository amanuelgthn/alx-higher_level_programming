#!/usr/bin/python3
"""Class Square with private instance size"""


class Square:
    """Class Square with private instance size"""
    def __init__(self, size=0):
        try:
            if isinstance(size) == True and size > 0:
                num = int(size)
                self.__size = num
            if size < 0:
                 raise Exception("size must be >= 0")
        except TypeError:
            print("size must be an integer")
        
