#!/usr/bin/python3
"""
A script that changes the name of a State object from database hbtn_0e_6_usa
- takes three arguments: mysql username, mysql password and database name
- imports State and Base from model_state - from model_state import State, Base
- connects to a MySQL server running on localhost:3306
- changes the name of the State where id = 2 to New Mexico
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
    session = scoped_session(sessionmaker(engine))
    state = session.query(State).where(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()
