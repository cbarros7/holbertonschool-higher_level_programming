#!/usr/bin/python3
"""
Adds the State object “Louisiana” to
the database hbtn_0e_6_usa
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

    # Add new record
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Query
    query = session.query(State).\
        order_by(State.id.desc()).first()

    # Print query
    print("{}".format(query.id))

    # Close session
    session.close()
