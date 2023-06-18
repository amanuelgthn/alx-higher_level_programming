#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_101_usa
- script that takes 3 arguments: mysql username, mysql password, mysql
  database name
- connects to MySQL server running on localhost:3306
- using only one query to the databse
- using the state relationship to access to the State object linked to
  the City object
- results are sorted by ascending order of cities.id
- results are displayed as <city id>: <city name> -> <state name>
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session
from sqlalchemy.orm import scoped_session
from relationship_state import State, Base
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    session = scoped_session(sessionmaker(bind=engine))
    states = session.query(State).join(City).order_by(City.id)
    for state in states:
        for city in state.cities:
            print('{}: {} -> {}'.format(city.id, city.name, state.name))
    session.close()
