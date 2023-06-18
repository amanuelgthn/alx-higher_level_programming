#!/usr/bin/python3
"""
Python file similar to the model_state.py name model_state.py
that contains the class definition of a city
"""

from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
import sys
import MySQLdb


class City(Base):
    """
    City class that inherits from Base
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    def __init__(self, name):
        self.name = name
