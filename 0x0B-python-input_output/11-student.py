#!/usr/bin/python3
"""
Module class Student
"""


class Student:
    """
    student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialiazation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that returns the dictionary description
        with simple data structure
        """
        dict_attr = self.__dict__.copy()
        if (type(attrs) == list and all(type(item) == str for item in attrs)):
            att_dict = {}
            for i in attrs:
                if i in dict_attr:
                    att_dict[i] = dict_attr[i]
            return att_dict
        return dict_attr

    def reload_from_json(self, json):
        """
        Public methon to replace all attributes of the student
        instance"""
        for item in json:
            self.__dict__[item] = json[item]
