#!/usr/bin/python3
"""script that deletes all State objects from the database"""

import sys
from model_state import Base, State

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqLdb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

""" delete object """
    objects = session.query(State).filter(State.name.contains('%a'))
    for obj in objects:
        session.delete(obj)
    session.commit()
    session.close()
