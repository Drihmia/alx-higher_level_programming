#!/usr/bin/env python3
""" a script that prints all City objects from the database hbtn_0e_14_usa

Results is be sorted in ascending order by "cities.id"

The code won't not be executed when imported.
"""

if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, sessionmaker
    from sys import argv

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(url.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()

    t_query = sess.query(City).group_by(City.id).order_by(City.id.asc())

    for city in t_query.all():
        state_name = sess.query(State).get(city.state_id).name
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    sess.close()
