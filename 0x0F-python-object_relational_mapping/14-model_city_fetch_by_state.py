#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from model_city import Base, City
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
    query = session.query(State, City).\
        filter(State.id == City.state_id).all()

    # Print qury --> s : state. c: city
    for s, c in query:
        print("{}: ({}) {}".format(s.name, c.id, c.name))

    # Close session
    session.close()
