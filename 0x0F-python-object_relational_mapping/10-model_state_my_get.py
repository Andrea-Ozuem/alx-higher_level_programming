#!/usr/bin/python3
''' prints the first State objects from the database hbtn_0e_6_usa;'''

import sys
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == sys.argv[4]).first()
    if states:
        print(states.id)
    else:
        print("Not found")
