#!/usr/bin/env python3
""" a script that changes the name of a "State" object
from the database  "hbtn_0e_6_usa"

Change the name of the State where id = 2 to New Mexico

The code won't not be executed when imported.

Usage: script <mysql UserName> <mysql PassWord> <mysql DatabaseName>
"""

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine, delete
    from sqlalchemy.orm import Session, sessionmaker
    from sys import argv

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(url.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()

    states_to_delete = sess.query(State).where(State.name.like('%a%')).all()
    for state in states_to_delete:
        sess.delete(state)

    # commit changes
    sess.commit()

    sess.close()
