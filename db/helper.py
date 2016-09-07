# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation
# TODO - replace prints with logs for the lumberjack

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
from sqlalchemy import create_engine, MetaData
from db.models import Base, BankAccount, Contract, EmailAddress, Letter, \
    Relation, Transaction, Type, User
from colorama import Fore, Back, Style

from dialogs import SettingsDialog

import logging
Lumberjack = logging.getLogger(__name__)


class DbHelper(object):

    session = None
    engine = None

    def __init__(self, *args):
        Lumberjack.info('spawning the <<< DbHelper >>>, he says: There can be only one!')
        self.settings = QSettings()

        db_file = os.path.join(self.settings.value('db_base_path'), self.settings.value('db_name'))
        db_string = 'sqlite:///{db_file}'.format(db_file=db_file)
        Lumberjack.debug('__init__ - db_file = {}'.format(db_file))
        if os.path.exists(db_file):
            self.engine = create_engine(db_string)
        else:
            Lumberjack.warning('__init__ - database not found')
            settings_dialog = SettingsDialog()
            settings_dialog.exec_()

    def create_new_db(self):

        engine = self.engine

        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        self.create_types()

    def create_types(self):
        # TODO - integrate with db settings from app. Type are not only for testing
        engine = create_engine('sqlite:///db/db_development.db')
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # Insert types into db
        type_list = [['Appointment', 'Job contract', 'Bank'],
                     ['Bill', 'Insurance', 'Employer'],
                     ['Contract', 'Loan', 'Housing'],
                     ['Information', None, 'Insurance'],
                     [None, None, 'IRS'],
                     [None, None, 'Medical'],
                     [None, None, 'Shop'],
                     [None, None, 'Subscription']]
        for type in type_list:
            new_type = Type(letter=type[0], contract=type[1], relation=type[2])
            session.add(new_type)

        session.commit()

    def get_app_db_session(self):
        if self.session:
            print(Fore.YELLOW + '====== RETURNING THE EXISTING SESSION =======')
            return self.session

        DBSession = sessionmaker(bind=self.engine)
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

    def get_table_statistics(self):
        session = self.get_app_db_session()
        table_list = {}

        tables = [BankAccount, Contract, EmailAddress, Letter,
                  Relation, Transaction, Type, User]

        for table in tables:
            print(Fore.YELLOW + 'Table name: ', table)
            row_count = session.query(table).count()
            table_list[table.__name__] = row_count
            print(Fore.YELLOW + '---Total table rowcount: ', row_count)
        print(Fore.YELLOW + '--Returning Table List: ', table_list)

        return table_list


class DbFileHandler(object):

    def __init__(self, *args):
        Lumberjack.info('spawning a << DbFileHandler >>')
        self.settings = QSettings()

    def store_file(self, mapper_file_name, file_projection):
        Lumberjack.info('< DbFileHandler > - -> (store_file)')
        print(Back.GREEN + 'Storing File: ', mapper_file_name, ', for: ', file_projection)
        print(Back.GREEN + 'ROOT_DIR = ', ROOT_DIR)
        if not mapper_file_name:
            return None
        db_path_type = self.settings.value('db_type')
        db_path = self.settings.value('db_base_path')
        if db_path_type == 0:
            db_dir_path = os.path.join(ROOT_DIR, db_path, file_projection[0])
        print(Back.GREEN + 'DB_dir_path = ', db_dir_path)
        if not os.path.isdir(db_dir_path):
            os.makedirs(db_dir_path)

        full_file_name = os.path.join(db_dir_path, file_projection[1])
        print(Back.GREEN + 'full file name = ', full_file_name)
        print(Back.GREEN + 'with type = ', type(full_file_name))
        print(Back.GREEN + 'mapper_file_name = ', mapper_file_name)
        print(Back.GREEN + 'with type = ', type(mapper_file_name))
        if not os.path.exists(full_file_name) or mapper_file_name[0] != full_file_name:
            copyfile(mapper_file_name[0], full_file_name)

        return full_file_name


class TableMaker:
    table_data = []
    header_data = []


