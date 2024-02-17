#!/usr/bin/python3
""" a python file that contains the class definition of a "city" and an
instance Base imported from model_state:
    *city class:
        - inherits from Base
        - links to the MySQL table cities
        - class attribute "id" that represents a column of an auto-generated,
            unique integer, can’t be null and is a primary key
        - class attribute "name" that represents a column of a string
            with maximum 128 characters and can’t be null
        - class attribute state_id that represents a column of an integer,
            can’t be null and is a foreign key to states.id
"""
from relationship_state import Base
from sqlalchemy import (Integer, String, Column, ForeignKey)


class City(Base):
    """ A class that define the city linked to cities table in MySQL """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    # def __init__(self, state_id, name):
    # """init methode for adding the name to database"""
    # self.state_id = state_id
    # self.name = name
