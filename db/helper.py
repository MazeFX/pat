# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: helper.py
Creator: MazeFX
Date: 4-8-2016

Python Test docstring.
"""

from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from db.models import Base, User, Letter


def create_new_db():

    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine('sqlite:///db/db_development.db')

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)

    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    # A DBSession() instance establishes all conversations with the database
    # and represents a "staging zone" for all the objects loaded into the
    # database session object. Any change made against the objects in the
    # session won't be persisted into the database until you call
    # session.commit(). If you're not happy about the changes, you can
    # revert all of them back to the last commit by calling
    # session.rollback()
    session = DBSession()

    # Insert a Person in the person table
    new_user = User(name='MazeFX', fullname='MazeFX the Greatest', password='Test')
    session.add(new_user)
    session.commit()

    # Insert an Address in the address table
    new_letter = Letter(sender='Een geldwolf', user='1')
    session.add(new_letter)
    session.commit()
