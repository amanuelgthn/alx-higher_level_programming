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
    - class attribute cities represents a relationship with the class City. If the State object is deleted
      all linked City objects are automatically deleted. The reference from a City object to this State named state
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from relationship_city import City, Base
import sys
import MySQLdb


class State(Base):
    """
    state class that inherits from Base
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    
    cities = relationship("City", backref="state")
    
