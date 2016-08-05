# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: forms.py
Creator: MazeFX
Date: 1-8-2016

Python Test docstring.
"""
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget

from MyQtness.ui_letter_form import Ui_LetterForm


class LetterForm(QWidget, Ui_LetterForm):

    def __init__(self, *kwargs):
        super(LetterForm, self).__init__(*kwargs)

        self.setupUi(self)
        # TODO  - Create own functions for loading the rc file, own style
        self.pushButtonAdd.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonAdd.clicked.connect(self.on_add)
        self.pushButtonReset.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonReset.clicked.connect(self.on_reset)

    def on_add(self):
        print('Add signal sent and recieved.')


    def on_reset(self):
        print('Reset signal sent and recieved.')