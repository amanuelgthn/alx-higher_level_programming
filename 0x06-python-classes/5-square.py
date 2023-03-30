#!/usr/bin/python3
"""Class Square with private instance size"""


class Square:
    """Class Square with private instancef size"""
    def __init__(self, size=0):
        self.__size = size

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

    def area(self):
        """Public instance method to return area of square"""
        return self.size**2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(0, self.size):
                for j in range(0, self.__size):
                    print("#",end="")
                print()
