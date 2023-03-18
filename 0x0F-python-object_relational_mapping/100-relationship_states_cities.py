#!/usr/bin/python3
''' lists all State objects from the database hbtn_0e_6_usa;'''

import sys
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="California", cities=[City(name="San Francisco")])
    session.add(state)
    session.commit()
