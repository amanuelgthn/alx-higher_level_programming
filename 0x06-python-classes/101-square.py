#!/usr/bin/python3
"""Class Square with private instance size"""


class Square:
    """Class Square with private instancef size"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Public instance method to return area of square"""
        return self.size**2

    def __str__(self):
        result = ""
        if self.size == 0:
            return "\n"
        else:
            for y in range(0, self.position[1]):
                result += "\n"
            for i in range(0, self.size):
                for j in range(0, self.size+self.position[0]):
                    if j < self.position[0]:
                        result += " "
                    else:
                        result += "#"
                result += "\n"
            return result[:-1]

    def my_print(self):
        print(self.list_print(), end="")
