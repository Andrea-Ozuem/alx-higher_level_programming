#!/usr/bin/python3
''' changes the name of a State object in the database hbtn_0e_6_usa;'''

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
    i = session.query(State).get(2)
    i.name = "New Mexico"
    session.add(i)
    session.commit()
