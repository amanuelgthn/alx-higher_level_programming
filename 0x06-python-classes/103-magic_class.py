#!/usr/bin/python3
import math
"""math module to import pi"""


class MagicClass:
    """MagicClass to calculate area and circumfurence of a circle"""
    def __init__(self, radius):
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        return self._MagicClass__radius ** 2 * math.pi

    def circumfurence(self):
        return 2 * math.pi * self._MagicClass__radius
