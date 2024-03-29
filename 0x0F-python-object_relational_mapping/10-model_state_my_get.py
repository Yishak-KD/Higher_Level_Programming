#!/usr/bin/python3
"""Script that prints the State object with name passed as argument"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).all()

    for i in result:
        if sys.argv[4] == i.name:
            print(i.id)
            break
    else:
        print("Not found")
