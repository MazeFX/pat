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
from MyQtness.myWidgets import myTableView


class LetterTab(QWidget):

    def __init__(self, *kwargs):
        super(LetterTab, self).__init__(*kwargs)

        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = myTableView(self)
        self.letterForm = LetterForm()
        self.horizontalLayout.addWidget(self.letterForm)
        self.horizontalLayout.addWidget(self.tableView)

        self.setLayout(self.horizontalLayout)
