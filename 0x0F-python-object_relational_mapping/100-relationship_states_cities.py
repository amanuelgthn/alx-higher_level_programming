#!/usr/bin/python3
"""
A script that creates the State "California" with the City "San Francisco" from the database htbtn_0e_100_usa
- Takes 3 arguments: mysql username, mysql password, database name
- connects to MySQL server running on localhost:3306
- use the cities relationship for all State 
"""


import sys
import MySQLdb
from relationship_state import State, City, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    session = scoped_session(sessionmaker(bind=engine))
    Base.metadata.create_all(engine)
    state = State(name='California')
    session.add(state)
    city = City(name='San Francisco')
    session.add(city)
    session.commit()
    session.close()
    
   
