#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
- import State and Base from model_state- from model_state import State, Base
- connects to a MySQL server running on localhost at port 3306
- Results are sorted in ascending order by states.id
"""


import sys
import MySQLdb
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    session = scoped_session(sessionmaker(bind=engine))
    states = session.query(State).order_by(State.id).all()
    for state in states:
        if "a" in state.name:
            print('{}: {}'.format(state.id, state.name))
