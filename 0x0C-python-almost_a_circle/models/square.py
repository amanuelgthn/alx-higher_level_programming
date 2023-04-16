#!/usr/bin/python3
"""
import module Rectangle
"""


from models.rectangle import Rectangle
"""
Module containing Square class
"""


class Square(Rectangle):
    """
    Square class inheriting from base class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        __str__ method
        """
        result = ""
        result = "[" + str(type(self).__name__) + "] " + "("
        result += str(self.id) + ") " + str(self.x) + "/" + str(self.y) + " - "
        result += str(self.size)
        return result

    def __update(self, id=None, size=None, x=None, y=None):
        if id:
            self.id = id
        if size:
            self.size = size
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
        dict_attr['size'] = self.size
        return dict_attr