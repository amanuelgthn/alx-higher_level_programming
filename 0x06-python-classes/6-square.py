#!/usr/bin/python3
"""Class Square with private instance size"""


class Square:
    """Class Square with private instancef size"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) != int or value[0] < 0
              or type(value[1]) != int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Public instance method to return area of square"""
        return self.size**2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for y in range(0, self.position[1]):
                print()
            for i in range(0, self.size):
                for j in range(0, self.size+self.position[0]):
                    if j < self.position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()
