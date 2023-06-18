#!/usr/bin/python3
"""
A script that adds the State object "Louisiana" to the database htbn_0e_6_usa
- takes 3 arguments: mysql username, mysql password, database name
- imports State and Base from model_state- from model_state import State, Base
- connects to a MySQL server running on localhost at port 3306
- print the new state.id after creation
"""


import sys
import MySQLdb
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    session = scoped_session(sessionmaker(bind=engine))
    Base.metadata.create_all(engine)
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    session.close()
    states = session.query(State).order_by(State.id).filter(
        State.name == 'Louisiana').all()
    for state in states:
        print(state.id)
