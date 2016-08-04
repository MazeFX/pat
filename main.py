# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: main.py
Creator: MazeFX
Date: 3-8-2016

Main file for Personal Admin Tool.

For initialisation of the main application and handling
login events. Populating the main window with the necessary
sub-forms and widgets.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import qdarkstyle

from dialogs import LoginDialog
from MyQtness.ui_main_window import Ui_MainWindow


class MainApp(QMainWindow, Ui_MainWindow):

    def __init__(self, *kwargs):
        super(MainApp, self).__init__(*kwargs)

        self.setupUi(self)
        # TODO  - Create own functions for loading the rc file, own style
        stylesheet = qdarkstyle.load_stylesheet_pyqt5()
        self.setStyleSheet(stylesheet)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    loginDialog = LoginDialog()

    isAuth = False
    result = -1
    while not isAuth:
        result = loginDialog.exec_()

        if result == loginDialog.Success or result == LoginDialog.Rejected:
            isAuth = True

        else:
            isAuth = False


    if result == loginDialog.Success:
        w = MainApp()
        w.show()
        app.exec_()

    sys.exit(-1)
