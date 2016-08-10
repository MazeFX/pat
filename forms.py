# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: forms.py
Creator: MazeFX
Date: 1-8-2016

Python Test docstring.
"""
from PyQt5.QtCore import Qt, QDate, QByteArray
from PyQt5.QtWidgets import QWidget, QDataWidgetMapper

from db.models import AlchemicalTableModel, User
from db.helper import DbHelper
from MyQtness.ui_letter_form import Ui_LetterForm



class LetterForm(QWidget, Ui_LetterForm):

    def __init__(self, *kwargs):
        super(LetterForm, self).__init__(*kwargs)

        self.setupUi(self)
        # TODO  - Create own functions for loading the rc file, own style

        self.pushButtonAdd.setFocusPolicy(Qt.NoFocus)
        self.pushButtonAdd.clicked.connect(self.on_add)

        self.pushButtonEdit.setFocusPolicy(Qt.NoFocus)
        self.pushButtonEdit.clicked.connect(self.on_edit)

        self.pushButtonDelete.setFocusPolicy(Qt.NoFocus)
        self.pushButtonDelete.clicked.connect(self.on_delete)

        self.pushButtonSave.setFocusPolicy(Qt.NoFocus)
        self.pushButtonSave.clicked.connect(self.on_save)

        self.pushButtonReset.setFocusPolicy(Qt.NoFocus)
        self.pushButtonReset.clicked.connect(self.on_reset)

        self.toggle_edit_mode(False, None)

    def setModel(self, model):
        self.model = model

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.dateDateEdit, 0)
        self.mapper.addMapping(self.subjectLineEdit, 1)
        self.mapper.addMapping(self.senderComboBox, 2)
        self.mapper.addMapping(self.referenceLineEdit, 3)
        self.mapper.addMapping(self.userComboBox, 4)

        self.set_controls()

    def set_controls(self):
        user_model = AlchemicalTableModel(
            DbHelper().get_db_session(),
            User,
            [('Full Name', User.fullname, 'fullname', {})])
        self.userComboBox.setModel(user_model)
        self.userComboBox.setModelColumn(0)
        self.userComboBox.currentIndexChanged.connect(self.selectionchange)

    def selectionchange(self, index):
        print('chosen index: ', index)
        self.userComboBox.setRootModelIndex(index)

    def toggle_edit_mode(self, flag, mode):
        print('Setting edit mode for letter form: ', flag, mode)
        self.edit_mode = mode
        self.dateDateEdit.setEnabled(flag)
        self.subjectLineEdit.setEnabled(flag)
        self.senderComboBox.setEnabled(flag)
        self.referenceLineEdit.setEnabled(flag)
        self.userComboBox.setEnabled(flag)
        self.scanFileDrop.setEnabled(flag)

    def on_add(self):
        print('Add signal sent and recieved.')
        row = self.model.rowCount(None)
        self.model.insertNewRow(row)
        self.mapper.setCurrentIndex(row)
        now = QDate.currentDate()
        self.dateDateEdit.setDate(now)
        self.subjectLineEdit.setFocus()
        self.toggle_edit_mode(True, 'add')
        print('New row at index: ', row)
        print('mapper index: ', self.mapper.currentIndex())

    def on_edit(self):
        print('Edit signal sent and recieved.')
        self.mapper.setCurrentIndex(1)
        print('mapper index: ', self.mapper.currentIndex())
        self.toggle_edit_mode(True, 'edit')

    def on_delete(self):
        print('Delete signal sent and recieved.')

    def on_save(self):
        print('Save signal sent and recieved.')
        if self.edit_mode == 'add':
            self.mapper.submit()
        if self.edit_mode == 'edit':
            self.mapper.submit()
        self.toggle_edit_mode(False, None)

    def on_reset(self):
        print('Reset signal sent and recieved.')
