#!/usr/bin/python3
"""
Module containing Class MyInt
"""


class MyInt(int):
    """
    MyInt class
    """

    def __init__(self, int_num):
        """
        Inittialization
        """
        self.int_num = int_num

    @property
    def int_num(self):
        return self.__int_num

    @int_num.setter
    def int_num(self, int_num):
        if type(int_num) is int:
            self.__int_num = int_num

    def __eq__(self, other):
        if self.int_num == other:
            return False
        else:
            return True

    def __ne__(self, other):
        if self.int_num != other:
            return False
        else:
            return True
