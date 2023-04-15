#!/usr/bin/python3
"""
Module containing the class BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
Module containing the class BaseGeometry
"""


class Square(Rectangle):
    """
    This is the square class
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        str_print = ""
        str_print = "[Rectangle]" + str(self.__size) + "/" + str(self.__size)
        return str_print
