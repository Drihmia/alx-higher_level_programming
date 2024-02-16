#!/usr/bin/python3
""" a script that lists all "State" objects from the database "hbtn_0e_6_usa"

that contain the letter a

The "state" you display must be the first in "states.id"

Nothing followed by a new line will be printed if the table states is empty
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

    t_query = sess.query(State).where(State.name.like("%a%"))
    letter_a = t_query.order_by(State.id.asc())
    results = letter_a.all()
    if (results):
        for s in results:
            print("{}: {}".format(s.id, s.name))

    sess.close()
