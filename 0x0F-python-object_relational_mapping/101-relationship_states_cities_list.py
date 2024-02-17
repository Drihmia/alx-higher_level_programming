#!/usr/bin/python3
""" a script that lists all State objects, and corresponding City
    objects, contained in the database hbtn_0e_101_usa

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

    states = sess.query(State).order_by(State.id).all()
    for state in states:
        print(str(state.id) + ":", state.name)
        cities = sorted(state.cities, key=lambda city: city.id, reverse=False)
        for city in cities:
            print("\t" + str(city.id) + ":", city.name)

    sess.close()
