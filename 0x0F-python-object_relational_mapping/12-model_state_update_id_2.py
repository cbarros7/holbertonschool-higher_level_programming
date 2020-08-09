#!/usr/bin/python3
"""
changes the name of a State
object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Initialize engine
    Base.metadata.create_all(engine)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Update record
    update = session.query(State).filter(State.id == 2).one()
    update.name = "New Mexico"
    session.commit()

    # Close session
    session.close()
