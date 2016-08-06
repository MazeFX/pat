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


def create_test_db():

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
    new_letter1 = Letter(date=None,
                         sender='Een geldwolf',
                         user='1',
                         reference='Reference for 1',
                         scan_file='Scan file path')
    session.add(new_letter1)
    new_letter2 = Letter(date=None,
                         sender='Een geldwolf',
                         user='1',
                         reference='Reference for 2',
                         scan_file='Scan file path')
    session.add(new_letter2)
    new_letter3 = Letter(date=None,
                         sender='Een geldwolf',
                         user='1',
                         reference='Reference for 3',
                         scan_file='Scan file path')

    session.add(new_letter3)
    session.commit()


def get_db_session():
    engine = create_engine('sqlite:///db/db_development.db')

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


def get_table(model):
    tablemaker = TableMaker()
    print('tablemaker created.')
    tablemaker.header_data = model.get_headers_for_qt(model)
    print('header_data passed', tablemaker.header_data)
    session = get_db_session()
    table = session.query(model).order_by(model.date_created)
    data = []
    for letter in table:
        row_data = letter.convert_for_qt()
        data.append(row_data)
    print('tHis is the data list: ', data)
    tablemaker.table_data = data

    return tablemaker


class TableMaker:
    table_data = []
    header_data = []
