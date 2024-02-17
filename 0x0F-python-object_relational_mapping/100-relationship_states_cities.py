#!/usr/bin/python3
""" a script that creates the State “California” with the City “San Francisco”
    from the database "hbtn_0e_100_usa"

Usage: script <mysql UserName> <mysql PassWord> <mysql DatabaseName>
"""


if __name__ == "__main__":
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Session
    from sys import argv

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(url.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sess = Session()

    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    sess.add(california)
    sess.add(san_francisco)

    # to_del = sess.query(State).filter(State.id == 11).all()
    # for i in to_del:
    # sess.delete(i)

    sess.commit()
    sess.close()
