#!/usr/bin/python3
"""Script that lists all objects that contain the a letter from the database"""

import sys
from model_state import Base, State

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqLdb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

""" Output the result """
    states = session.query(State).filter(State.name.like(sys.argv[4]))
    if states.count() != 1 or not states:
        print("Not found")
    else:
        print("{}".format(states.first().id))
