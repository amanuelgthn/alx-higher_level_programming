#!/usr/bin/python3
"""
a script that lists all State objects, and corresponding city objects
contained in the databaese hbtn_0e_101_usa
- takes 3 argumetns: mysql username, mysql password, and database name
- connects to MySQL server to localhost:3306
- only uses one query
- use cities relationship for all state objects
- results are sorted by cities.id and states.id
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from relationship_state import State, City, Base


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    session = scoped_session(sessionmaker(bind=engine))
    states = session.query(State).order_by(State.id)
    for state in states:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('    {}: {}'.format(city.id, city.name))
    session.close()
