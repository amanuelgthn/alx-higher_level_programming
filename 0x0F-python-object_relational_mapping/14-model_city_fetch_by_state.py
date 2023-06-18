#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa
- takes 3 arguments: mysql username,mysql password,database name
- imports State and Base from model_state - from model_state import Base, State
- connects to a MySQL server running on localhost:3306
- Results are sorted in ascending order by cities.id
- Results are displayed in the format <state name>: (<city id>) <city name>)
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    session = scoped_session(sessionmaker(bind=engine))
    cities = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
