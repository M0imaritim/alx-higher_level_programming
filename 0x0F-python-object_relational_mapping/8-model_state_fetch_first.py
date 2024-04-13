#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                              argv[2],
                                                              argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    if states:
        for state in states:
            if states[0]:
                print("{}: {}".format(state.id, state.name))
                break
    else:
        print()
