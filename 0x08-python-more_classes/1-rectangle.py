#!/usr/bin/python3
"""
Module for Class Rectangle
class Rectangle that defines a width and height
"""


class Rectangle:
    """
    class Rectangle that defines a width and height
    """

    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Property for private instance attribute:width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property setter for private instance attribute:width
        """
        if(type(value)) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Property for private instance attribute:height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Property setter for private instance attribute:height
        """
        if(type(value)) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
