#!/usr/bin/python3
"""Class Square with private instance size"""


class Square:
    """Class Square with private instance size"""
    def __init__(self, size=0):
            if isinstance(size) == False:
                raise TypeError("size must be an integer")
            elif size < 0:
                 raise ValueError("size must be >= 0")
            else:
                self.__size = size
             
        
