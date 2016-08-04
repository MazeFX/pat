# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: helper.py
Creator: MazeFX
Date: 4-8-2016

Python Test docstring.
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.models import Base, User, Letter


def create_new_db():

    engine = create_engine('sqlite:///db/db_development.db')

    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Insert a Person in the person table
    new_user = User(name='MazeFX', fullname='MazeFX the Greatest', password='Test')
    session.add(new_user)
    session.commit()

    # Insert an Address in the address table
    new_letter = Letter(sender='Een geldwolf', user='1')
    session.add(new_letter)
    session.commit()


def get_db_session():
    engine = create_engine('sqlite:///db/db_development.db')

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session
