#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
- imports State and Base from model_state -
  from model_state import Base, State
- connects to a MySQL server running on localhost at port 3306
"""


import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = scoped_session(sessionmaker(bind=engine))
    Base.metadata.create_all(engine)
    states = session.query(State).filter(State.name.contains('a'))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
