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

    entites = sess.query(City, State).join(State).order_by(City.id).all()
    for entite in entites:
        city, state = entite
        print(str(city.id) + ":", city.name, "->", state.name)
    sess.close()
