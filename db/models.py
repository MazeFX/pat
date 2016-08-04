# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: models.py
Creator: MazeFX
Date: 3-8-2016

Python Test docstring.
"""


from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return "<User(id= '%s', name='%s', fullname='%s')>" % (
            self.id, self.name, self.fullname)


class Letter(Base):
    __tablename__ = 'letter'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    sender = Column(String(250))
    user = Column(Integer, ForeignKey('user.id'), nullable=False)
    reference = Column(String(250))
    scan_file = Column(String(250))

