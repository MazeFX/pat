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

from db.models import AlchemicalTableModel, User, Relation
from db.helper import DbHelper, DbFileHandler
from MyQtness.ui_letter_form import Ui_LetterForm
from MyQtness.myWidgets import MyItemDelegate


class LetterForm(QWidget, Ui_LetterForm):

    dbhelper = None

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
        self.mapper.addMapping(self.scanFileDrop, 5)

        self.set_controls()

    def set_controls(self):
        session = self.dbhelper.get_app_db_session()
        user_model = AlchemicalTableModel(
            session,
            User,
            [('Full Name', User.fullname, 'fullname', {})])

        relation_model = AlchemicalTableModel(
            session,
            Relation,
            [('Name', Relation.name, 'name', {})])

        delegate = MyItemDelegate(self)
        self.mapper.setItemDelegate(delegate)
        self.userComboBox.setModel(user_model)
        self.senderComboBox.setModel(relation_model)

    def toggle_edit_mode(self, flag, mode):
        print('Setting edit mode for letter form: ', flag, mode)
        self.edit_mode = mode
        self.dateDateEdit.setEnabled(flag)
        self.subjectLineEdit.setEnabled(flag)
        self.senderComboBox.setEnabled(flag)
        self.referenceLineEdit.setEnabled(flag)
        self.userComboBox.setEnabled(flag)
        self.scanFileDrop.setEnabled(flag)

    def set_mapper_index(self, *args):
        print('Setting letter Form mapper index: ', args)
        selected_index = args[0].indexes()
        row_index = selected_index[0].row()
        self.mapper.setCurrentIndex(row_index)
        print('Setting letter Form mapper index: ', row_index)

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
        print('mapper index: ', self.mapper.currentIndex())
        self.toggle_edit_mode(True, 'edit')

    def on_delete(self):
        print('Delete signal sent and recieved.')

    def on_save(self):
        print('Save signal sent and recieved.')
        self.check_scanned_file()
        if self.edit_mode == 'add':
            self.mapper.submit()
        if self.edit_mode == 'edit':
            self.mapper.submit()
        self.toggle_edit_mode(False, None)

    def check_scanned_file(self):
        print('Scanning for file in db protocol.')
        mapper_file_name = self.scanFileDrop.getCurrentFile()
        print('Mapper file name = ', mapper_file_name)
        projection_dir = str(self.senderComboBox.currentItem.name)
        projection_name = '{date}_{sender}_{reference}.pdf'.format(
            date=self.dateDateEdit.date().toPyDate(),
            sender=self.senderComboBox.currentItem.name,
            reference=self.referenceLineEdit.text())
        print('File Projection = ', (projection_dir, projection_name))
        stored_file = DbFileHandler().store_file(mapper_file_name, (projection_dir, projection_name))
        print('stored file = ', stored_file)
        print('with type = ', type(stored_file))
        self.scanFileDrop.setCurrentFile(stored_file)

    def on_reset(self):
        print('Reset signal sent and recieved.')
