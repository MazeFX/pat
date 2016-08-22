# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: forms_refactor.py
Creator: MazeFX
Date: 22-8-2016

Python Test docstring.
"""

from PyQt5.QtCore import Qt, QDate, QModelIndex
from PyQt5.QtWidgets import QWidget, QDataWidgetMapper

from db.models import AlchemicalTableModel, User, Relation
from db.helper import DbHelper, DbFileHandler
from MyQtness.ui_letter_form import Ui_LetterForm
from MyQtness.ui_relation_form import Ui_RelationForm
from MyQtness.ui_user_form import Ui_UserForm
from MyQtness.myWidgets import MyItemDelegate
from dialogs import SaveDialog

from colorama import Fore, Back, Style


class BasicForm(QWidget):

    dbhelper = None

    def __init__(self, *kwargs):
        super(BasicForm, self).__init__(*kwargs)

        self.setupUi(self)
        self.edit_mode = None

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


    def setModel(self, model):
        self.model = model

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)

        #

        delegate = MyItemDelegate(self)
        self.mapper.setItemDelegate(delegate)
        self.mapper.setCurrentIndex(0)

        self.toggle_edit_mode(False, None, None)
        self.set_controls()

    def set_controls(self):
        pass
