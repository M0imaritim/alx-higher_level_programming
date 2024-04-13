#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    my_sess = Session()
    for state in my_sess.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    my_sess.close()
