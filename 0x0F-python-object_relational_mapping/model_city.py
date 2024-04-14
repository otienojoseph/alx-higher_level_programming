#!/usr/bin/python3
"""This module contains City class"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String


Base = declarative_base()


class City(Base):
    """
    City class which inherits Base class

    Attributes:
        id (int) - Represents column of the auto generated,
            unique integer, can't be null and is primary key
        name (str) - Represents column of string with maximum
            128 characters and can't be null
        state_id (int) - Represents the column of an integer, can't
            be null and is a foreign key to 'states.id'
    """

    __tablename__ = "cities"

    id = Column(
        Integer, primary_key=True, unique=True, nullable=False,
        autoincrement=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
