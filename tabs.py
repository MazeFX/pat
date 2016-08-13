# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: tabs.py
Creator: MazeFX
Date: 5-8-2016

Python Test docstring.
"""

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTableView

from forms import LetterForm
from db.models import AlchemicalTableModel, Letter
from MyQtness.myWidgets import MyTableView
from MyQtness.ui_home_tab import Ui_HomeTab
from colorama import Fore, Back, Style


class LetterTab(QWidget):

    dbhelper = None

    def __init__(self, dbhelper, **kwargs):
        super(LetterTab, self).__init__(**kwargs)
        self.dbhelper = dbhelper

        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        print('Lettertab horizontal view created.')

        model = AlchemicalTableModel(
            self.dbhelper.get_app_db_session(),
            Letter,
            [('Date', Letter.date, 'date', {}),
             ('Subject', Letter.subject, 'subject', {}),
             ('Sender', Letter.sender, 'sender.name', {}),
             ('Reference', Letter.reference, 'reference', {}),
             ('User', Letter.user, 'user.fullname', {}),
             ('Letter Scan', Letter.scan_file, 'scan_file', {}),
             ('Date created', Letter.date_created, 'date_created', {})])

        print('Letter Tab model role names: ', model.roleNames())

        self.tableView = MyTableView()
        self.tableView.setModel(model)

        self.letterForm = LetterForm()
        self.letterForm.dbhelper = self.dbhelper
        self.letterForm.setModel(model)

        self.horizontalLayout.addWidget(self.letterForm)
        self.horizontalLayout.addWidget(self.tableView)

        self.setLayout(self.horizontalLayout)


class HomeTab(QWidget, Ui_HomeTab):

    def __init__(self, *args):
        super(HomeTab, self).__init__(*args)

        self.setupUi(self)
        # TODO - test font implementation on headers
