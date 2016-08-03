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
from PyQt5.QtGui import QApplication
from logindialog import LoginDialog
from mainwindow import MainWindow
import helper

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    helper.dbConnect()

    loginDialog = LoginDialog()

    isAuth = False
    result = -1
    while not isAuth:
        result = loginDialog.exec_()
        if result == LoginDialog.Success or result == LoginDialog.Rejected:
            isAuth = True
        else:
            isAuth = False

    if result == LoginDialog.Success:
        w = MainWindow()
        w.show()
        a.exec_()

    sys.exit(-1)