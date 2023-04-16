#!/usr/bin/python3
"""
import json module
"""


import json
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
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        cls_name = ""
        cls_name = cls.__name__+ ".json"
        #if list_objs:
            #list_objs = Base.to_json_string(list_objs)
        with open(cls_name,'w',encoding="utf-8") as file:
            file.write(str(list_objs))
