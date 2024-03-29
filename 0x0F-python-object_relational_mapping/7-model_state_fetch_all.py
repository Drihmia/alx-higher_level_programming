#!/usr/bin/python3
""" a script that lists all "State" objects from the database "hbtn_0e_6_usa"

Results is be sorted in ascending order by "states.id"

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

    t_query = sess.query(State).group_by(State.id).order_by(State.id.asc())
    for s in t_query.all():
        print("{}: {}".format(s.id, s.name))
    sess.close()
