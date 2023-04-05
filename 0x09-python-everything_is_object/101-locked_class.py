#!/usr/bin/python3
"""
Module containing LockedClass class to preventing the user
from dynamically creating new instance attributes except for
first_name"""


class LockedClass:
   """
   LockedClass
   """
   __slots__= ['first_name']
