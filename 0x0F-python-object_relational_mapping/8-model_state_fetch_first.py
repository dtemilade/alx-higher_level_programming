#!/usr/bin/python3
"""Script that lists firts objects from a database using alchemy"""

import sys
from model_state import Base, State

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if _u_name__ == "__main__":
     engine = create_engine("mysql+mysqldb ://{}:{}@localhost:3306/{}".format(
         sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    """ Output the result """
    retval = session.query(State).first()
    print("{}: {}".format(states.id, states.name))
