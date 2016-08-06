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
from db.models import Letter
from db.helper import get_table
from MyQtness.myWidgets import myTableView


class LetterTab(QWidget):

    def __init__(self, *args):
        super(LetterTab, self).__init__(*args)

        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        print('Lettertab horizontal view created.')
        tableViewTable = get_table(Letter)
        print('TableViewTable is created.', tableViewTable)
        self.tableView = myTableView(self, tableViewTable)
        print('myTableView in lettertab is present.')
        self.letterForm = LetterForm()
        self.horizontalLayout.addWidget(self.letterForm)
        self.horizontalLayout.addWidget(self.tableView)

        self.setLayout(self.horizontalLayout)
