#!/usr/bin/python3
""" a script that adds the State object “Louisiana” to
the database "hbtn_0e_6_usa"

Print the new states.id after creation

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

    state_1 = State("Louisiana")
    sess.add(state_1)
    sess.commit()

    print(state_1.id)

    sess.close()
