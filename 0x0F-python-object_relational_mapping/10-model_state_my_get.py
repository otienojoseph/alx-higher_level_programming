#!/usr/bin/python3
"""
    Script that lists all State objects from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def listStates(user, password, db, state_name):
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, password, db),
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # create a session
    session = Session()

    # extract all states
    state = session.query(State).order_by(State.id).filter(
         State.name.ilike(state_name)).all()

    try:
        print(state[0].id)
    except IndexError:
        print("Not found")

    session.close()


if __name__ == "__main__":
    [user_name, password, db_name, state] = sys.argv[1:]
    listStates(user=user_name, password=password, db=db_name,
               state_name=state)
