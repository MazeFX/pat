# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: helper.py
Creator: MazeFX
Date: 4-8-2016

Python Test docstring.
"""

import os
import datetime
from shutil import copyfile

from PyQt5.QtCore import QSettings

from constants import ROOT_DIR
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.models import Base, User, Letter, Relation
from colorama import Fore, Back, Style


class DbHelper(object):

    session = None

    db_base_path = None

    def __init__(self, *args):
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
                             sender_id=1,
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
                             user_id=0,
                             scan_file='Scan file path',
                             letter_type=0)
        session.add(new_letter2)
        new_letter3 = Letter(date=datetime.date.today(),
                             sender_id=0,
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
            print(Fore.YELLOW + '====== RETURNING THE EXISTING SESSION =======')
            return self.session

        self.db_string = 'sqlite:///{base}{db}'.format(
            base=self.settings.value('db_base_path'),
            db=self.settings.value('db_name'))

        engine = create_engine(self.db_string)

        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()
        print(Fore.YELLOW + '====== CREATED A NEW SESSION =======')
        return self.session

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


class DbFileHandler(object):

    def __init__(self, *args):
        print('DbFileHandler Initialising')
        self.settings = QSettings()

    def store_file(self, mapper_file_name, file_projection):
        print('Storing File: ', mapper_file_name, ', for: ', file_projection)
        print('ROOT_DIR = ', ROOT_DIR)
        db_path_type = self.settings.value('db_type')
        db_path = self.settings.value('db_base_path')
        if db_path_type == 0:
            db_dir_path = os.path.join(ROOT_DIR, db_path, file_projection[0])
        print('DB_dir_path = ', db_dir_path)
        if not os.path.isdir(db_dir_path):
            os.makedirs(db_dir_path)

        full_file_name = os.path.join(db_dir_path, file_projection[1])
        print('full file name = ', full_file_name)
        print('with type = ', type(full_file_name))
        print('mapper_file_name = ', mapper_file_name)
        print('with type = ', type(mapper_file_name))
        if not os.path.exists(full_file_name):
            copyfile(mapper_file_name, full_file_name)

        return full_file_name


class TableMaker:
    table_data = []
    header_data = []


