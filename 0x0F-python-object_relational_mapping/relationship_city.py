#!/usr/bin/python3
"""
Python file similar to the model_state.py name model_state.py
that contains the class definition of a city
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
import sys
import MySQLdb


Base = declarative_base()


class City(Base):
    """
    City class that inherits from Base
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __init__(self, name):
        self.name = name
