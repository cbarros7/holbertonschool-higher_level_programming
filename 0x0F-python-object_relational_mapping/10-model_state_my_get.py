#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from
the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3], sys.argv[4]),
                           pool_pre_ping=True)

    # Initialize engine
    Base.metadata.create_all(engine)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).all()

    # Create all name for states
    list_state = []
    for state in query:
        list_state.append(state.name)

    # Query
    query = session.query(State).\
        filter(State.name == "{}".format(sys.argv[4], )).first()

    # Conditions
    if sys.argv[4] not in list_state:
        print("Not found")
    else:
        print(query.id)

    # Close session
    session.close()
