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
from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt

from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from colorama import Fore, Back, Style

from db.qvariantalchemy import String, Integer, DateTime, Date


Base = declarative_base()


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


class Letter(Base):
    __tablename__ = 'letters'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    sender_id = Column(Integer, ForeignKey('relations.id'), nullable=False)
    subject = Column(String(250))
    reference = Column(String(250))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    scan_file = Column(String(250))
    letter_type = Column(Integer)
    date_created = Column(DateTime, default=datetime.datetime.now)

    user = relationship('User', foreign_keys=[user_id])
    sender = relationship('Relation', foreign_keys=[sender_id])

    def __repr__(self):
        return "<Letter(id= '%s', sender='%s', subject='%s')>" % (
            self.id, self.sender, self.subject)


class Relation(Base):
    __tablename__ = 'relations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    reference = Column(String(250))
    bank_account = Column(String(250))
    relation_type = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    date_created = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<Relation(id= '%s', name='%s', reference='%s')>" % (
            self.id, self.name, self.reference)


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
        self.filter = filter
        self.refresh()

    def refresh(self):
        """Recalculates, self.results and self.count"""

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
        _flags = Qt.ItemIsEnabled | Qt.ItemIsSelectable

        if self.sort is not None:
            order, col = self.sort

            if self.fields[col][3].get('dnd', False) and index.column() == col:
                _flags |= Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled

        if self.fields[index.column()][3].get('editable', False):
            _flags |= Qt.ItemIsEditable

        return _flags

    def supportedDropActions(self):
        return Qt.MoveAction

    def dropMimeData(self, data, action, row, col, parent):
        if action != Qt.MoveAction:
            return

        return False

    def rowCount(self, parent):
        return self.count or 0

    def columnCount(self, parent):
        return len(self.fields)

    def get_column_index(self, name):
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
        if '.' in name:
            foreign_column = name.split('.')
            foreign_item = getattr(row, foreign_column[0])
            return str(getattr(foreign_item, foreign_column[1]))
        return getattr(row, name)

    def setData(self, index, value, role=None):
        print(Fore.BLUE + '-- setting data for: ', index, 'with value: ', value)
        print(Fore.BLUE + '-- index column', index.column(), 'with row: ', index.row())
        row = self.results[index.row()]
        name = self.fields[index.column()][2]

        if '.' in name:
            name = name.split('.')[0]

        if index.column() == 4:
            print(Fore.BLUE + '====== setting the user =======')
            print(Fore.BLUE + '-- sending value : ', value)
            print(Fore.BLUE + '-- with type : ', type(value))
            print(Fore.BLUE + '-- While current: ', getattr(row, name))
            print(Fore.BLUE + '-- with type : ', type(getattr(row, name)))

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
        self.sort = order, col
        self.refresh()

    def createNewRow(self, index):
        print('createNewRow from model is called.')
        new_row = []
        for x in self.fields:
            new_row.append('')
        self.results.append(new_row)

    def insertNewRow(self, index):
        new_object = self.model()
        new_object.user = 0
        '''
        for x in range(len(self.fields)):
            setattr(new_object, self.fields[x][2], self.result[index][x])
        print('newobject = ', new_object)
        '''
        self.session.add(new_object)
        self.session.commit()
        self.refresh()


