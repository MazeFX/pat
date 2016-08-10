# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: helper.py
Creator: MazeFX
Date: 4-8-2016

Python Test docstring.
"""

from PyQt5.QtCore import QSettings

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.models import Base, User, Letter


class DbHelper(object):

    def __init__(self, *args):
        super(DbHelper, self).__init__(*args)
        self.settings = QSettings()


    def create_test_db(self):

        engine = create_engine('sqlite:///db/db_development.db')

        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # Insert a Person in the person table
        new_user = User(name='Nick', fullname='Nick Geense', password='Test')
        session.add(new_user)
        new_user = User(name='Stefanie', fullname='Stefanie Lacet', password='Test')
        session.add(new_user)
        session.commit()

        # Insert an Address in the address table
        new_letter1 = Letter(date=None,
                             sender='Een geldwolf',
                             user_id=1,
                             reference='Reference for 1',
                             scan_file='Scan file path')
        session.add(new_letter1)
        new_letter2 = Letter(date=None,
                             sender='Een geldwolf',
                             user_id=2,
                             reference='Reference for 2',
                             scan_file='Scan file path')
        session.add(new_letter2)
        new_letter3 = Letter(date=None,
                             sender='Een geldwolf',
                             user_id=1,
                             reference='Reference for 3',
                             scan_file='Scan file path')

        session.add(new_letter3)
        session.commit()

    def get_db_session(self):
        chosen_database = self.settings.value('db_name', type='int')
        if chosen_database == 0:
            self.db_string = 'sqlite:///db/db_development.db'
        elif chosen_database == 1:
            self.db_string = 'sqlite:///c:/PAT_db_files/PAT_db.db'

        engine = create_engine(self.db_string)

        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        return session

    def get_table(self, model):
        tablemaker = TableMaker()
        print('tablemaker created.')
        tablemaker.header_data = model.get_headers_for_qt(model)
        print('header_data passed', tablemaker.header_data)
        session = self.get_db_session()
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
