# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: forms.py
Creator: MazeFX
Date: 1-8-2016

Python Test docstring.
"""
from PyQt5.QtWidgets import QWidget

import qdarkstyle
from MyQtness.ui_letter_form import Ui_LetterForm


class LetterForm(QWidget, Ui_LetterForm):

    def __init__(self, *kwargs):
        super(LetterForm, self).__init__(*kwargs)

        self.setupUi(self)
        # TODO  - Create own functions for loading the rc file, own style
        #stylesheet = qdarkstyle.load_stylesheet_pyqt5()
        #self.setStyleSheet(stylesheet)
