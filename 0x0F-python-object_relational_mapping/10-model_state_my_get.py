#!/usr/bin/python3
""" a script that prints the "State" object with the name passed
as argument
from the database "hbtn_0e_6_usa"


The "state" you display must be the first in "states.id"
If no state has the name searched for, a Not found message will be displayed.


Usage: script\
        <mysql UserName> <mysql PassWord> <mysql DatabaseName>\
        <mysql StateName> (searched + safe from MySQL injection)

The code won't not be executed when imported.
"""

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, sessionmaker
    from sys import argv

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(url.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()

    sName = argv[4]
    # handling the case where the sName contain a single quote
    index = sName.find(";")
    if (index >= 0):
        sName = sName[:index]

    t_query = sess.query(State).filter(State.name == sName)
    letter_a = t_query.group_by(State.id).order_by(State.id.asc())
    states = letter_a.all()
    if (states):
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")
    sess.close()
