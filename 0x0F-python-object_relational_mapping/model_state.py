#!/usr/bin/python3
"""This module contains State class"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """
    State class which inherits Base class

    Attributes:
        id (int) - Represents column of the auto generated,
            unique integer, can't be null and is primary key
        name (str) - Represents column of string with maximum
            128 characters and can't be null
    """

    __tablename__ = "states"

    id = Column(
        Integer, primary_key=True, unique=True, nullable=False,
        autoincrement=True
    )
    name = Column(String(128), nullable=False)
