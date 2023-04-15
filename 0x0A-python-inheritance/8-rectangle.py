#!/usr/bin/python3
"""
Module containing the class BaseGeometry
"""


class BaseGeometry:
    """
    This is the BaseGeometry class
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
