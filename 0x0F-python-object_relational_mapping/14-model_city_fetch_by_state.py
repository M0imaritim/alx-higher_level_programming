#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == '__main__':
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                              argv[2],
                                                              argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State, City).join(City).order_by(State.id).all()
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
