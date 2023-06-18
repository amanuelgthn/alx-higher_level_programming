#!/usr/bin/python3
"""
A script tht prints the first State onject from the database htbtn_0e_6_usa
- takes three arguments mysql username, mysql password and database name
- import State and Base from model_state- from model_state import State, Base
- connect to MySQL server running on localhost at port 3306
- state displayed is the first in state.id
- not allowed to fetch all states from database before displaying the result
- if table states is empty print nothing follwed bt a new line
"""

import sys
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from model_state import State, Base


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    session = scoped_session(sessionmaker(bind=engine))
    states = session.query(State).where(State.id == 1).first()
    if states is None:
        print()
        return
    print('{}: {}'.format(states.id, states.name))
