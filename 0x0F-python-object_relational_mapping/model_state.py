#!/usr/bin/python3
"""Class definition of a State"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class State(Base):
	"""Class of State"""
	__tablename__ = 'states'
	id = Column(Integer, primary_key=True)
	name = Column(String(128), nullable= False)
