#!/usr/bin/python3
"""
Module containing the class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
Module containing the class BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    This is the BaseGeometry class
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
