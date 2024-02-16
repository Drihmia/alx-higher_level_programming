#!/usr/bin/env python3
""" a script that changes the name of a "State" object
from the database  "hbtn_0e_6_usa"

Change the name of the State where id = 2 to New Mexico

The code won't not be executed when imported.

Usage: script <mysql UserName> <mysql PassWord> <mysql DatabaseName>
"""

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine, update
    from sqlalchemy.orm import Session, sessionmaker
    from sys import argv

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(url.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()

    # the id is unique so the output is always one query (lenght of 1)
    # using condition only for rest assured.
    # states = sess.query(State).filter(State.id == 2).all()
    # for state in states:
    # if state.id == 2:
    # state.name = "New Mexico"
    # sess.add(state)
    # sess.commit()

    # 2nd method, using update method directly
    sess.query(State).filter(State.id == 2).update({'name': 'New Mexico'})
    sess.commit()

    sess.close()
