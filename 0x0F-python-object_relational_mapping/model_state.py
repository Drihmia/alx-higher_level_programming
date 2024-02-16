#!/usr/bin/python3
""" a python file that contains the class definition of a "State" and an
instance Base = declarative_base():
    *State class:
        -inherits from Base Tips
        -links to the MySQL table states
        -class attribute "id" that represents a column of an auto-generated,
            unique integer, can’t be null and is a primary key
        -class attribute "name" that represents a column of a string
            with maximum 128 characters and can’t be null
"""
from sqlalchemy import (Integer, String, Column)
from sqlalchemy.orm import (declarative_base)


Base = declarative_base()


class State(Base):
    """ A class that define the State linked to states table in MySQL """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        """init methode for adding the name to database"""
        self.name = name
