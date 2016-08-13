# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: helper.py
Creator: MazeFX
Date: 4-8-2016

Python Test docstring.
"""

import datetime

from PyQt5.QtCore import QSettings

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.models import Base, User, Letter, Relation


class DbHelper(object):

    session = None

    def __init__(self, *args):
        super(DbHelper, self).__init__(*args)
        self.settings = QSettings()

    def create_test_db(self):

        engine = create_engine('sqlite:///db/db_development.db')

        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # Insert Users in the user table
        new_user = User(name='Nick', fullname='Nick Geense', password='Test')
        session.add(new_user)
        new_user = User(name='Stefanie', fullname='Stefanie Lacet', password='Test')
        session.add(new_user)
        session.commit()

        # Insert Letters in the letter table
        new_letter1 = Letter(date=datetime.date.today(),
                             sender_id=0,
                             subject='About 1',
                             reference='Reference for 1',
                             user_id=1,
                             scan_file='Scan file path',
                             letter_type=0)
        session.add(new_letter1)
        new_letter2 = Letter(date=datetime.date.today(),
                             sender_id=0,
                             subject='About 2',
                             reference='Reference for 2',
                             user_id=2,
                             scan_file='Scan file path',
                             letter_type=0)
        session.add(new_letter2)
        new_letter3 = Letter(date=datetime.date.today(),
                             sender_id=1,
                             subject='About 3',
                             reference='Reference for 3',
                             user_id=1,
                             scan_file='Scan file path',
                             letter_type=0)
        session.add(new_letter3)

        # Insert Relations in the relation table
        new_relation1 = Relation(name='ING',
                                 fullname='ING Bank B.V.',
                                 reference='Reference for ING',
                                 bank_account='This is where the money goes',
                                 relation_type=0,
                                 start_date=datetime.date.today(),
                                 end_date=datetime.date.today() + datetime.timedelta(days=360))
        session.add(new_relation1)
        new_relation2 = Relation(name='Ziekenfonds',
                                 fullname='Ziekenfonds United Ltd.',
                                 reference='Reference for Ziekenfonds',
                                 bank_account='This is where the money goes',
                                 relation_type=0,
                                 start_date=datetime.date.today(),
                                 end_date=datetime.date.today() + datetime.timedelta(days=360))
        session.add(new_relation2)
        session.commit()

    def get_app_db_session(self):
        if self.session:
            return self.session
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
        session = self.get_app_db_session()
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
