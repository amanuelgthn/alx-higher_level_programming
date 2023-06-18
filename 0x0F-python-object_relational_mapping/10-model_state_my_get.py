#!/usr/bin/python3
"""
A script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
- takes 4 arguments; mysql username, mysql password, database
  name and state name to search (SQL injection free)
- mport States and Base from model_state-
  from model_state import State, Base
- connects to a MySQL server running on localhost at port 3306
- results must display the state.id
- if no state has the name searched for, display Not Found
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
    state_name = format(sys.argv[4]).encode('utf-8')
    states = session.query(State).order_by(State.id).filter(
        State.name == state_name).all()
    printed = False
    for state in states:
        if state.id:
            print(state.id)
            printed = True
    if not printed:
        print("Not Found")
