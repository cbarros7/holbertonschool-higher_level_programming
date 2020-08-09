#!/usr/bin/python3
"""
Prints the first State object from the
database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Initialize engine
    Base.metadata.create_all(engine)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    query = session.query(State).first()

    # Print query
    if query is None:
        print("Nothing")
    else:
        print("{}: {}".format(query.id, query.name))

    # Close session
    session.close()
