#!/usr/bin/python3
"""
    Script that lists all City objects from the database hbtn_0e_14_usa
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def listStates(user, password, db):
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, password, db),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # create a session
    session = Session()

    # extract all states cities
    cities = session.query(State, City).filter(State.id == City.state_id)

    # print all cities
    for city in cities:
        print("{}: ({}) {}".format(city.State.name, city.City.id,
                                   city.City.name))

    session.close()


if __name__ == "__main__":
    [user_name, password, db_name] = sys.argv[1:]
    listStates(user=user_name, password=password, db=db_name)
