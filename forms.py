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

import qdarkstyle
from MyQtness.ui_letter_form import Ui_letter_form


class LetterForm(QtWidgets.QMainWindow):

    def __init__(self, *kwargs):
        super(LetterForm, self).__init__(*kwargs)

        self.qtness = Ui_letter_form()
        self.qtness.setupUi(self)
        # TODO  - Create own functions for loading the rc file, own style
        stylesheet = qdarkstyle.load_stylesheet_pyqt5()
        self.setStyleSheet(stylesheet)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    main = LetterForm()
    main.show()
    sys.exit(app.exec_())
