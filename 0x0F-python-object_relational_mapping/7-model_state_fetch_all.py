#!/usr/bin/python3
# Script that lists all state objects from a database

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
	engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
	Base.metadata.create_all(engine)
	
	session = Session(engine)

	for state in session.query(State).order_by(State.id):
        	print("{}: {}".format(state.id, state.name))
