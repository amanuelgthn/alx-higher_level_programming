#!/usr/bin/python3
"""
import module Base
"""


from models.base import Base
"""
Module containing Rectangle class
"""


class Rectangle(Base):
    """
    rectangle class inheriting from base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        self.__id = id
        super().__init__(self.__id)

    @property
    def width(self):
        """
        Property for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property setter for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Property for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Property setter for height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Property for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Property setter for x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Property for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Property setter for y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        method that returns area of a rectangle
        """
        return self.height * self.width

    def display(self):
        """
        method that prints rectangle with the character #
        """
        for k in range(0, self.y):
            print()
        for i in range(0, self.height):
            for j in range(self.x, self.width + self.x):
                print("#", end="")
            print()

    def __str__(self):
        """
        __str__ method
        """
        result = ""
        result = "[" + str(type(self).__name__) + "] " + "("
        result += str(self.id) + ") " + str(self.x) + "/" + str(self.y) + " - "
        result += str(self.width) + "/" + str(self.height)
        return result

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        if id:
            self.id = id
        if width:
            self.width = width
        if height:
            self.height = height
        if x:
            self.x = x
        if y:
            self.y = y

    def update(self, *args, **kwargs):
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        dict_attr = {}
        dict_attr['x'] = self.x
        dict_attr['y'] = self.y
        dict_attr['id'] = self.id
        dict_attr['height'] = self.height
        dict_attr['width'] = self.width
        return dict_attr

