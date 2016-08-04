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
from PyQt5 import QtWidgets
from dialogs import LoginDialog
from MyQtness.ui_main_window import Ui_MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    loginDialog = LoginDialog()

    isAuth = False
    result = -1
    while not isAuth:
        result = loginDialog.exec_()
        if result == loginDialog.Success or result == loginDialog.Rejected:
            isAuth = True
        else:
            isAuth = False

    if result == loginDialog.Success:
        w = Ui_MainWindow()
        w.show()
        app.exec_()

    sys.exit(-1)
