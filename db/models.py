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

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QVariant, Qt

from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from colorama import Fore, Back, Style

import logging
Lumberjack = logging.getLogger(__name__)

from db.qvariantalchemy import Boolean, Currency, String, Integer, DateTime, Date


Base = declarative_base()


class BankAccount(Base):
    __tablename__ = 'bank_accounts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bank_name = Column(String)
    account = Column(String)
    balance = Column(Integer)
    date_created = Column(DateTime, default=datetime.datetime.now)

    user = relationship('User', foreign_keys=[user_id])

    def __repr__(self):
        return "<BankAccount(id= '%s', name='%s', account='%s')>" % (
            self.id, self.bank_name, self.account)

    def load_dummy(self):
        self.user_id = 1
        self.bank_name = ''
        self.account = ''
        self.balance = 0


class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True)
    relation_id = Column(Integer, ForeignKey('relations.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_id = Column(Integer, ForeignKey('bank_accounts.id'), nullable=False)
    letter_id = Column(Integer, ForeignKey('letters.id'), nullable=False)
    reference = Column(String(250))
    email_id = Column(Integer, ForeignKey('e_addresses.id'), nullable=False)
    contract_type_id = Column(Integer, ForeignKey('types.id'))
    total_amount = Column(Integer)
    recur_amount = Column(Integer)
    recurrence = Column(DateTime)
    start_date = Column(Date)
    end_date = Column(Date)
    date_created = Column(DateTime, default=datetime.datetime.now)

    relation = relationship('Relation', foreign_keys=[relation_id])
    user = relationship('User', foreign_keys=[user_id])
    account = relationship('BankAccount', foreign_keys=[account_id])
    letter = relationship('Letter', foreign_keys=[letter_id])
    email = relationship('EmailAddress', foreign_keys=[email_id])
    contract_type = relationship('Type', foreign_keys=[contract_type_id])

    def __repr__(self):
        return "<Contract(id= '%s', relation='%s', reference='%s')>" % (
            self.id, self.relation, self.reference)

    def load_dummy(self):
        self.relation_id = 1
        self.user_id = 1
        self.account_id = 1
        self.letter_id = 1
        self.reference = ''
        self.email_id = 1
        self.contract_type_id = 1
        self.total_amount = 0
        self.recur_amount = 0
        self.recurrence = 0
        self.start_date = datetime.date.today()
        self.end_date = datetime.date.today()


class EmailAddress(Base):
    __tablename__ = 'e_addresses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    address = Column(String)
    date_created = Column(DateTime, default=datetime.datetime.now)

    user = relationship('User', foreign_keys=[user_id])

    def __repr__(self):
        return "<EmailAddress(id= '%s', user='%s', address='%s')>" % (
            self.id, self.user, self.address)

    def load_dummy(self):
        self.user_id = 1
        self.address = ''


class Letter(Base):
    __tablename__ = 'letters'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    relation_id = Column(Integer, ForeignKey('relations.id'), nullable=False)
    subject = Column(String(250))
    reference = Column(String(250))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    scan_file = Column(String(250))
    letter_type_id = Column(Integer, ForeignKey('types.id'))
    date_created = Column(DateTime, default=datetime.datetime.now)

    user = relationship('User', foreign_keys=[user_id])
    relation = relationship('Relation', foreign_keys=[relation_id])
    letter_type = relationship('Type', foreign_keys=[letter_type_id])

    def __repr__(self):
        return "<Letter(id= '%s', relation='%s', subject='%s')>" % (
            self.id, self.relation, self.subject)

    def load_dummy(self):
        self.date = datetime.date.today()
        self.relation_id = 1
        self.subject = ''
        self.reference = ''
        self.user_id = 1
        self.scan_file = ''
        self.letter_type_id = 1


class Relation(Base):
    __tablename__ = 'relations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    reference = Column(String(250))
    bank_account = Column(String(250))
    relation_type_id = Column(Integer, ForeignKey('types.id'))
    date_created = Column(DateTime, default=datetime.datetime.now)

    relation_type = relationship('Type', foreign_keys=[relation_type_id])

    def __repr__(self):
        return "<Relation(id= '%s', name='%s', reference='%s')>" % (
            self.id, self.name, self.reference)

    def load_dummy(self):
        self.name = ''
        self.fullname = ''
        self.reference = ''
        self.bank_account = ''
        self.relation_type_id = 1


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    contract_id = Column(Integer, ForeignKey('contracts.id'))
    letter_id = Column(Integer, ForeignKey('letters.id'), nullable=False)
    account_id = Column(Integer, ForeignKey('bank_accounts.id'), nullable=False)
    amount = Column(Currency)
    transaction_date = Column(Date)
    payment_date = Column(Date)
    payment_state = Column(Boolean)
    debit = Column(Boolean)
    date_created = Column(DateTime, default=datetime.datetime.now)

    contract = relationship('Contract', foreign_keys=[contract_id])
    letter = relationship('Letter', foreign_keys=[letter_id])
    account = relationship('BankAccount', foreign_keys=[account_id])

    def __repr__(self):
        return "<Transaction(id= '%s', account='%s', ammount='%s')>" % (
            self.id, self.account, self.ammount)

    def load_dummy(self):
        self.contract_id = 1
        self.letter_id = 1
        self.account_id = 1
        self.amount = 0
        self.transaction_date = datetime.date.today()
        self.payment_date = None
        self.payment_state = False
        self.debit = False


class Type(Base):
    __tablename__ = 'types'

    id = Column(Integer, primary_key=True)
    letter = Column(String)
    contract = Column(String)
    relation = Column(String)
    date_created = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<Type(id= '%s', letter='%s', relation='%s')>" % (
            self.id, self.letter, self.relation)

    def load_dummy(self):
        self.letter = ''
        self.relation = ''


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<User(id= '%s', name='%s', fullname='%s')>" % (
            self.id, self.name, self.fullname)

    def load_dummy(self):
        self.name = ''
        self.fullname = ''
        self.password = ''


class AlchemicalTableModel(QAbstractTableModel):
    """
    A Qt Table Model that binds to a SQL Alchemy query

    Example:
    >>> model = AlchemicalTableModel(Session, [('Name', Entity.name)])
    >>> table = QTableView(parent)
    >>> table.setModel(model)
    """

    def __init__(self, session, model, columns):
        super(AlchemicalTableModel, self).__init__()
        Lumberjack.info('spawning a << AlchemicalTableModel >>')
        #TODO self.sort_data = None
        self.session = session
        self.fields = columns
        self.query = session.query(model)
        self.model = model

        self.results = None
        self.count = None
        self.sort = None
        self.filter = None

        self.refresh()

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.fields[col][0])
        return QVariant()

    def setFilter(self, filter):
        """Sets or clears the filter, clear the filter by setting to None"""
        Lumberjack.info('< AlchemicalTableModel > - -> (setFilter)')
        self.filter = filter
        self.refresh()

    def refresh(self):
        """Recalculates, self.results and self.count"""
        Lumberjack.info('< AlchemicalTableModel > - -> (refresh)')

        self.layoutAboutToBeChanged.emit()

        q = self.query
        if self.sort is not None:
            order, col = self.sort
            col = self.fields[col][1]
            if order == Qt.DescendingOrder:
                col = col.desc()
        else:
            col = None

        if self.filter is not None:
            q = q.filter(self.filter)

        q = q.order_by(col)

        self.results = q.all()
        self.count = q.count()
        self.layoutChanged.emit()

    def flags(self, index):
        Lumberjack.debug('< AlchemicalTableModel > - -> (flags)')
        _flags = Qt.ItemIsEnabled | Qt.ItemIsSelectable

        if self.sort is not None:
            order, col = self.sort

            if self.fields[col][3].get('dnd', False) and index.column() == col:
                _flags |= Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled

        if self.fields[index.column()][3].get('editable', False):
            _flags |= Qt.ItemIsEditable

        return _flags

    def supportedDropActions(self):
        Lumberjack.info('< AlchemicalTableModel > - -> (supportedDropActions)')
        return Qt.MoveAction

    def dropMimeData(self, data, action, row, col, parent):
        Lumberjack.info('< AlchemicalTableModel > - -> (dropMimeData)')
        if action != Qt.MoveAction:
            return

        return False

    def rowCount(self, parent):
        Lumberjack.debug('< AlchemicalTableModel > - -> (rowCount)')
        return len(self.results) or 0

    def columnCount(self, parent):
        Lumberjack.debug('< AlchemicalTableModel > - -> (columnCount)')
        return len(self.fields)

    def get_column_index(self, name):
        Lumberjack.debug('< AlchemicalTableModel > - -> (get_column_index)')
        for x in range(len(self.fields)):
            if name == self.fields[x][2]:
                return x
        print('TableModel - No column index found')
        return None

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        elif role not in (Qt.DisplayRole, Qt.EditRole):
            return QVariant()

        row = self.results[index.row()]
        name = self.fields[index.column()][2]
        # IDEA  - This could be done better. Need to ponder a bit..
        if self.fields[index.column()][3].get('type', False):
            field_type = self.fields[index.column()][3]['type']
            if field_type == 'currency':
                if role == Qt.EditRole:
                    return getattr(row, name)
                value = str(getattr(row, name))
                value = '€ {},{}'.format(value[:-2], value[-2:])
                return value

        # TODO - create function for displaying scanfile present icon.
        # TODO - create function to display currencies.
        if '.' in name:
            foreign_column = name.split('.')
            foreign_item = getattr(row, foreign_column[0])
            if role == Qt.EditRole:
                print('TableModel - data -- EditRole for foreignkey with index: ', index)
                return foreign_item
            else:
                if foreign_item is None:
                    return None
                return getattr(foreign_item, foreign_column[1])
        if role == Qt.EditRole:
            print('TableModel - data -- EditRole for index: ', index)
            print('TableModel - data -- EditRole with value: ', getattr(row, name))
            print('TableModel - data -- EditRole with value: ', type(getattr(row, name)))
            return getattr(row, name)
        return str(getattr(row, name))

    def setData(self, index, value, role=None):
        row = self.results[index.row()]
        name = self.fields[index.column()][2]
        if '.' in name:
            name = name.split('.')[0]

        try:
            setattr(row, name, value)
            self.session.commit()
        except Exception as ex:
            QMessageBox.critical(None, 'SQL Error', str(ex))
            return False
        else:
            self.dataChanged.emit(index, index)
            return True

    def sort(self, col, order):
        """Sort table by given column number."""
        Lumberjack.info('< AlchemicalTableModel > - -> (sort)')
        # TODO - create sort for foreign key columns
        self.sort = order, col
        self.refresh()

    def createNewRow(self, index):
        Lumberjack.info('< AlchemicalTableModel > - -> (createNewRow)')
        new_row = []
        for x in self.results:
            new_row.append('')
        self.results.append(new_row)

    def insertRow(self, row, parent=None, *args, **kwargs):
        Lumberjack.info('< AlchemicalTableModel > - -> (insertRow)')
        print(Fore.BLUE + '-- Projecting New Row --')
        print(Fore.BLUE + '-- Current results: ', self.results)
        print("\n\t\t ...insertRows() Starting position: '%s'" % row)
        new_object = self.model()
        print("\n\t\t ...dummy made: '%s'" % new_object)
        new_object.load_dummy()
        print("\n\t\t ...dummy loaded: '%s'" % new_object)
        self.beginInsertRows(QModelIndex(), row, row)
        self.results.append(new_object)
        self.endInsertRows()
        print(Fore.BLUE + '-- Current results: ', self.results)
        return True

    def rollbackRow(self, row):
        Lumberjack.info('< AlchemicalTableModel > - -> (rollbackRow)')
        self.results.pop()
        self.refresh()

    def storeRow(self, row):
        Lumberjack.info('< AlchemicalTableModel > - -> (storeRow)')
        new_object = self.results[row]
        self.session.add(new_object)
        self.session.commit()

    def removeRow(self, row, parent=None, *args, **kwargs):
        Lumberjack.info('< AlchemicalTableModel > - -> (removeRow)')
        print("\n\t\t ...removeRows() Starting position: '%s'" % row)
        self.beginRemoveRows(QModelIndex(), row, row)
        item = self.results[row]
        self.session.delete(item)
        self.session.commit()
        self.endRemoveRows()
        self.refresh()

        return True


