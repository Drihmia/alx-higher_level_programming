#!/usr/bin/python3
""" a script that lists the 1st "State" objects from the db "hbtn_0e_6_usa"

The "state" displayed is the first in "states.id"

"Nothing" followed by a new line will be printed if the table states is empty
The code won't not be executed when imported.

Usage: script <mysql UserName> <mysql PassWord> <mysql DatabaseName>
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

    results = sess.query(State).first()
    if (results):
        print("{}: {}".format(results.id, results.name))
    else:
        print("Nothing")

    sess.close()
