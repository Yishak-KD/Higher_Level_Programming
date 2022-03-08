#!/usr/bin/python3
"""
ORM SqlAlchemy
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()


class State(Base):
    """
    Class State which creates a table called states
    """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
