# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: dialogs.py
Creator: MazeFX
Date: 3-8-2016

Python Test docstring.
"""

from PyQt5.QtCore import QSettings

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

import qdarkstyle

from auth import Auth
from MyQtness.ui_login_dialog import Ui_LoginDialog
from MyQtness.ui_settings_dialog import Ui_SettingsDialog


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


class SettingsDialog(QDialog, Ui_SettingsDialog):
    Rejected, Success, Failed = range(0, 3)

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.currentDatabaseComboBox.addItems(['DB for development',
                                               'DB for storage'])

        self.load_settings()

        stylesheet = qdarkstyle.load_stylesheet_pyqt5()
        self.setStyleSheet(stylesheet)

        self.buttonBox.accepted.connect(self.on_accept)
        self.buttonBox.rejected.connect(self.on_reject)

    def load_settings(self):
        self.settings = QSettings()

        chosen_database = self.settings.value('db_type', type='int')
        self.currentDatabaseComboBox.setCurrentIndex(chosen_database)

    def on_accept(self):
        chosen_database = self.currentDatabaseComboBox.currentIndex()
        self.settings.setValue('db_type', chosen_database)
        if chosen_database == 0:
            self.settings.setValue('db_name', 'db_development.db')
            self.settings.setValue('db_base_path', 'db/db_files/')
        if chosen_database == 1:
            self.settings.setValue('db_name', 'PAT_db.db')
            self.settings.setValue('db_base_path', 'c:/PAT_db_files/')

        self.setResult(self.Success)

    def on_reject(self):
        self.setResult(self.Rejected)



