#!/usr/bin/python3
"""
import json module
import csv module
"""


import json
import csv
import turtle
import time
"""
base.py
"""


class Base:
    """
    Base Class
    """

    nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.nb_objects += 1
            self.id = Base.nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        method that returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method hat writes the JSON string representation of list_objs to a file
        """
        file_name = "{}.json".format(cls.__name__)
        if list_objs:
            list_objs = [objs.to_dictionary() for objs in list_objs]
        else:
            return []
        with open(file_name, 'w', encoding="utf-8") as file:
            file.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        method that returns an instance with all attributes already set
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        method that returns an instance with all attributes already set
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            instance = Rectangle(4, 6)
        elif cls == Square:
            instance = Square(4)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        method that returns list of instances
        """
        from os import path
        file_name = "{}.json".format(cls.__name__)
        if not path.isfile(file_name):
            return []
        with open(file_name, "r", encoding="utf-8") as file:
            json_string = file.read()
            instances = []
        instances = [cls.create(**d) for
                     d in cls.from_json_string(json_string)]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        method that serializes to objects
        """
        from models.rectangle import Rectangle
        from models.square import Square
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, "w", encoding="utf-8") as file:
            file = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    file.writerow([obj.id, obj.width,
                                   obj.height, obj.x, obj.y])
            else:
                for obj in list_objs:
                    file.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        method that deserializes from CSV
        """
        from models.rectangle import Rectangle
        from models.square import Square
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, "r", encoding="utf-8") as file:
            obj = csv.reader(file)
            list_obj = []
            for row in obj:
                row = [int(i) for i in row]
                if cls.__name__ == "Rectangle":
                    obj = cls(row[1], row[2], row[3], row[4], row[0])
                else:
                    obj = cls(row[1], row[2], row[3], row[0])
                list_obj.append(obj)
            return list_obj

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        method that opens a window and draws all the rectangle and square
        """
        tur = turtle.Turtle()
        tur.color("white")
        turtle.Screen().colormode(255)
        tur.pensize(2)
        tur.setposition(0, 0)
        for rectangle in list_rectangles:
            tur.color("blue")
            tur.setpos((rectangle.x, rectangle.y + tur.pos()[1]))
            tur.forward(rectangle.width)
            tur.right(90)
            tur.forward(rectangle.height)
            tur.right(90)
            tur.forward(rectangle.width)
            tur.right(90)
            tur.forward(rectangle.height)
            tur.end_fill()
        for square in list_squares:
            tur.color("red")
            tur.begin_fill()
            tur.setpos((square.x +tur.pos()[0], square.y -tur.pos()[1]))
            tur.forward(square.size)
            tur.right(90)
            tur.forward(square.size)
            tur.right(90)
            tur.forward(square.size)
            tur.right(90)
            tur.forward(square.size)
            tur.end_fill()
        time.sleep(10)
        tur.hideturtle()
        tur.end_fill()
