# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: forms.py
Creator: MazeFX
Date: 1-8-2016

Python Test docstring.
"""
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QWidget, QDataWidgetMapper

from MyQtness.ui_letter_form import Ui_LetterForm
from MyQtness.myWidgets import MyTableModel
from db.helper import get_table
from db.models import Letter


class LetterForm(QWidget, Ui_LetterForm):

    def __init__(self, *kwargs):
        super(LetterForm, self).__init__(*kwargs)

        self.setupUi(self)
        # TODO  - Create own functions for loading the rc file, own style
        self.pushButtonAdd.setFocusPolicy(Qt.NoFocus)
        self.pushButtonAdd.clicked.connect(self.on_add)
        self.pushButtonReset.setFocusPolicy(Qt.NoFocus)
        self.pushButtonReset.clicked.connect(self.on_reset)

        tableViewTable = get_table(Letter)
        self.model = MyTableModel(tableViewTable.table_data, tableViewTable.header_data)
        self.mapper = QDataWidgetMapper(self)

        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.dateDateEdit, 1)
        self.mapper.addMapping(self.subjectLineEdit, 2)
        self.mapper.addMapping(self.UserLineEdit, 3)
        self.mapper.addMapping(self.senderLineEdit, 4)
        self.mapper.addMapping(self.referenceLineEdit, 5)

        row = self.model.rowCount(None)
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)
        now = QDate.currentDate()
        self.dateDateEdit.setDate(now)
        self.subjectLineEdit.setFocus()

    def on_add(self):
        self.mapper.submit()
        print('Add signal sent and recieved.')
        print(self.model.arraydata)


    def on_reset(self):
        print('Reset signal sent and recieved.')