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
from db.helper import DbHelper
from MyQtness.myWidgets import MyTableView
from MyQtness.ui_home_tab import Ui_HomeTab


class LetterTab(QWidget):

    def __init__(self, *args):
        super(LetterTab, self).__init__(*args)

        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        print('Lettertab horizontal view created.')

        model = AlchemicalTableModel(
            DbHelper().get_db_session(),
            Letter,
            [('Date', Letter.date, 'date', {}),
             ('Subject', Letter.subject, 'subject', {}),
             ('Sender', Letter.sender, 'sender', {}),
             ('Reference', Letter.reference, 'reference', {}),
             ('User', Letter.user, 'user', {}),
             ('Letter Scan', Letter.scan_file, 'scan_file', {}),
             ('Date created', Letter.date_created, 'date_created', {})])

        self.tableView = MyTableView()
        self.tableView.setModel(model)

        self.letterForm = LetterForm()
        self.letterForm.setModel(model)

        self.horizontalLayout.addWidget(self.letterForm)
        self.horizontalLayout.addWidget(self.tableView)

        self.setLayout(self.horizontalLayout)


class HomeTab(QWidget, Ui_HomeTab):

    def __init__(self, *kwargs):
        super(HomeTab, self).__init__(*kwargs)

        self.setupUi(self)
