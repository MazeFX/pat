# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: forms.py
Creator: MazeFX
Date: 1-8-2016

Python Test docstring.
"""

import sys
from PyQt5 import QtWidgets

import MyQtness.qss as qss
from MyQtness.ui_letter_form import Ui_letter_form


class LetterForm(QtWidgets.QMainWindow):

    def __init__(self, *kwargs):
        super(LetterForm, self).__init__(*kwargs)

        self.qtness = Ui_letter_form()
        self.qtness.setupUi(self)
        stylesheet = qss.get_style('style')
        self.setStyleSheet(stylesheet)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    main = LetterForm()
    main.show()
    sys.exit(app.exec_())
