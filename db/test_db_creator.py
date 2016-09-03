# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: test_db_creator.py
Creator: MazeFX
Date: 3-9-2016

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


def create_test_db():
    engine = create_engine('sqlite:///db_development.db')

    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    create_bank_accounts(session)
    create_contract(session)
    create_email_adresses(session)
    create_letters(session)
    create_relations(session)
    create_transactions(session)
    create_types(session)
    create_users(session)


def create_bank_accounts(session):
    new_account1 = BankAccount(user_id=1,
                               bank_name='ING',
                               account='NL123INGB12345678',
                               balance=10000)
    session.add(new_account1)
    new_account2 = BankAccount(user_id=2,
                               bank_name='TRIODOS',
                               account='NL36TRIO123456789',
                               balance=20000)
    session.add(new_account2)
    session.commit()


def create_contract(session):
    new_contract1 = Contract(relation_id=1,
                             user_id=1,
                             account_id=1,
                             letter_id=1,
                             reference='',
                             email_id=1,
                             contract_type_id=1,
                             total_amount=35000,
                             recur_amount=0,
                             recurrence={},
                             start_date=datetime.date.today(),
                             end_date=datetime.date.today())
    session.add(new_contract1)
    new_contract2 = Contract(relation_id=2,
                             user_id=2,
                             account_id=2,
                             letter_id=2,
                             reference='33548391-4483',
                             email_id=2,
                             contract_type_id=2,
                             total_amount=35000,
                             recur_amount=3000,
                             recurrence={'days': 4},
                             start_date=datetime.date.today(),
                             end_date=datetime.date.today())
    session.add(new_contract2)
    session.commit()


def create_email_adresses(session):
    new_email1 = EmailAddress(user_id=1,
                              address='filoplast@gmail.com')
    session.add(new_email1)
    new_email2 = EmailAddress(user_id=2,
                              address='stefanieLacet@hotmail.com')
    session.add(new_email2)
    session.commit()


def create_letters(session):
    # Insert Letters in the letter table
    new_letter1 = Letter(date=datetime.date.today(),
                         relation_id=1,
                         subject='About 1',
                         reference='Reference for 1',
                         user_id=1,
                         scan_file='',
                         letter_type_id=1)
    session.add(new_letter1)
    new_letter2 = Letter(date=datetime.date.today(),
                         relation_id=1,
                         subject='About 2',
                         reference='Reference for 2',
                         user_id=1,
                         scan_file='',
                         letter_type_id=1)
    session.add(new_letter2)
    new_letter3 = Letter(date=datetime.date.today(),
                         relation_id=1,
                         subject='About 3',
                         reference='Reference for 3',
                         user_id=1,
                         scan_file='Scan file path',
                         letter_type_id=1)
    session.add(new_letter3)


def create_relations(session):
    # Insert Relations in the relation table
    new_relation1 = Relation(name='ING',
                             fullname='ING Bank B.V.',
                             reference='Reference for ING',
                             bank_account='This is where the money goes',
                             relation_type_id=1)
    session.add(new_relation1)
    new_relation2 = Relation(name='Ziekenfonds',
                             fullname='Ziekenfonds United Ltd.',
                             reference='Reference for Ziekenfonds',
                             bank_account='This is where the money goes',
                             relation_type_id=1)
    session.add(new_relation2)
    session.commit()


def create_transactions(session):
    new_transaction1 = Transaction(contract_id=1,
                                   letter_id=1,
                                   account_id=1,
                                   amount=2000,
                                   transaction_date=datetime.date.today(),
                                   payment_date=None,
                                   payment_state=False,
                                   debit=False)
    session.add(new_transaction1)
    new_transaction2 = Transaction(contract_id=2,
                                   letter_id=2,
                                   account_id=2,
                                   amount=4500,
                                   transaction_date=datetime.date.today(),
                                   payment_date=datetime.date.today(),
                                   payment_state=True,
                                   debit=True)
    session.add(new_transaction2)
    session.commit()


def create_types(session):
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


def create_users(session):
    # Insert Users in the user table
    new_user = User(name='Nick', fullname='Nick Geense', password='Test')
    session.add(new_user)
    new_user = User(name='Stefanie', fullname='Stefanie Lacet', password='Test')
    session.add(new_user)
    session.commit()


if __name__ == "__main__":
    create_test_db()
