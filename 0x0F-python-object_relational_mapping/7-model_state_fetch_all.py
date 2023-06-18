#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
- Imports state and base from model_state.py-
- from model_state import State,Base
- Connects to MySQL server running on localhost at port 3306
- Results must be sorted in ascending order of state.id
"""


import sys
from model_state import Base, State
from sqlalchemy import Table
from sqlalchemy import (create_engine)
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


if __name__ == "__main__":
    """Creating an engine object acting as a central source of connection
    to the database provided in the arguments"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    """Creating a session that handles the current database which will
    serve as a factory for new session objects"""
    session = scoped_session(sessionmaker(bind=engine))
    """creating a query method that takes State as an argument"""
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))
