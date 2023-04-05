#!/usr/bin/python3
"""
This is the '3-say_my_name' module containing a function that 
prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Function to print  'My name is' if followed by
    <first_name> <last_name>
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
