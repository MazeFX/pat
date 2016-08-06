# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: models.py
Creator: MazeFX
Date: 3-8-2016

Python Test docstring.
"""


import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class QtConvert(object):

    def convert_for_qt(self):
        props = list(x for x in self.__dict__.keys() if not x.startswith('_'))
        props.sort()
        values = []
        for prop in props:
            x = getattr(self, prop)
            if x is not None:
                values.append(x)
            else:
                values.append('')
        print('values returned are: ', values)
        return values

    def get_headers_for_qt(self):
        props = list(x for x in self.__dict__.keys() if not x.startswith('_'))
        print('props for header are: ', props)
        props.sort()
        return props



class User(Base, QtConvert):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<User(id= '%s', name='%s', fullname='%s')>" % (
            self.id, self.name, self.fullname)


class Letter(Base, QtConvert):
    __tablename__ = 'letter'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    sender = Column(String(250))
    user = Column(Integer, ForeignKey('user.id'), nullable=False)
    reference = Column(String(250))
    scan_file = Column(String(250))
    date_created = Column(DateTime, default=datetime.datetime.now)

