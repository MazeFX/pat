# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: dialogs.py
Creator: MazeFX
Date: 3-8-2016

Python Test docstring.
"""

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

import qdarkstyle

from auth import Auth
from MyQtness.ui_login_dialog import Ui_LoginDialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8

except AttributeError:

    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


class LoginDialog(QDialog, Ui_LoginDialog):
    Rejected, Success, Failed = range(0, 3)

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        stylesheet = qdarkstyle.load_stylesheet_pyqt5()
        self.setStyleSheet(stylesheet)

        self.buttonBox.accepted.connect(self.on_accept)
        self.buttonBox.rejected.connect(self.on_reject)

    def on_accept(self):
        auth = Auth()
        if auth.doLogin(str(self.userNameLineEdit.text()), str(self.passwordLineEdit.text())):
            self.setResult(self.Success)
        else:
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle(_translate("LoginDialog", "PAT Login message", None))
            msgBox.setText(_translate("LoginDialog", "Either incorrect username and/or password. Try again!", None))
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            self.setResult(self.Failed)

    def on_reject(self):
        self.setResult(self.Rejected)