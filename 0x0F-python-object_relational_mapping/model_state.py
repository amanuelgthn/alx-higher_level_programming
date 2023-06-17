#!/usr/bin/python3
"""
- Python file that contains the class definition of a State
            and an instance Base  = declarative_base()
- State class
    - inherits from Base
    - links MySQL table states
    - class attribute id that represents a column of an auto-generated,
      unique integer and can't b null and is a primary key
    - class attribute name that represents a column of a string with
      maximum 128 characters and can't be null
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
import sys
import MySQLdb


Base = declarative_base()


class State(Base):
    """
    state class that inherits from Base
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
