#!/usr/bin/python3
"""
lists all City objects from the database hbtn_0e_101_usa
"""
from sys import argv
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                              argv[2],
                                                              argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).join(City).order_by(City.id).all()
    for state in results:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
