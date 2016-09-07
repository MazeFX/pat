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

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QDialogButtonBox

import qtawesome as qta

from auth import Auth
from MyQtness import style
from MyQtness.ui_login_dialog import Ui_LoginDialog
from MyQtness.ui_settings_dialog import Ui_SettingsDialog
from MyQtness.ui_save_dialog import Ui_SaveDialog
from MyQtness.ui_close_dialog import Ui_CloseDialog
from MyQtness.ui_delete_dialog import Ui_DeleteDialog
from MyQtness.ui_termination_dialog import Ui_TerminationDialog
from colorama import Fore, Back, Style

import logging
Lumberjack = logging.getLogger(__name__)

try:
    _encoding = QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


# TODO - change for all dialogs: window icon and title
# TODO  - Create base class with window attributes??


class LoginDialog(QDialog, Ui_LoginDialog):
    Rejected, Success, Failed = range(0, 3)

    def __init__(self):
        QDialog.__init__(self)
        Lumberjack.info('spawning a << LoginDialog >>')
        self.setupUi(self)

        style.set_window_style(self)

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

    def __init__(self, reason=None):
        QDialog.__init__(self)
        Lumberjack.info('spawning a << SettingsDialog >>')
        self.setupUi(self)
        self.currentDatabaseComboBox.addItems(['DB for development',
                                               'DB for storage'])

        self.load_settings()

        style.set_window_style(self)

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


class SaveDialog(QDialog, Ui_SaveDialog):
    Rejected, Success, Failed = range(0, 3)

    def __init__(self):
        QDialog.__init__(self)
        Lumberjack.info('spawning a << SaveDialog >>')
        self.setupUi(self)

        style.set_window_style(self)

        button_list = self.buttonBox.buttons()
        for button in button_list:
            button.setFocusPolicy(Qt.NoFocus)

        self.buttonBox.accepted.connect(self.on_accept)
        self.buttonBox.rejected.connect(self.on_reject)
        self.buttonBox.clicked.connect(self.on_click)

    def on_accept(self):
        Lumberjack.info('< SaveDialog > - -> (on_accept)')
        self.setResult(self.Success)

    def on_click(self, *args):
        Lumberjack.info('< SaveDialog > - -> (on_click)')
        button_role = self.buttonBox.buttonRole(args[0])
        if button_role == 2:
            self.done(self.Failed)

    def on_reject(self):
        Lumberjack.info('< SaveDialog > - -> (on_reject)')
        self.setResult(self.Rejected)


class CloseDialog(QDialog, Ui_CloseDialog):
    Rejected, Minimize, Exit = range(0, 3)

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        Lumberjack.info('spawning a << CloseDialog >>')

        style.set_window_style(self)

        self.buttonBox.addButton('Minimize', QDialogButtonBox.YesRole)
        self.buttonBox.addButton('Exit', QDialogButtonBox.AcceptRole)
        button_list = self.buttonBox.buttons()
        for button in button_list:
            button.setFocusPolicy(Qt.NoFocus)

        self.buttonBox.rejected.connect(self.on_reject)
        self.buttonBox.clicked.connect(self.on_click)

    def on_click(self, *args):
        Lumberjack.info('< CloseDialog > - -> (on_click)')
        button_role = self.buttonBox.buttonRole(args[0])
        if button_role == 5:
            self.done(self.Minimize)
        elif button_role == 0:
            self.done(self.Exit)

    def on_reject(self):
        Lumberjack.info('< CloseDialog > - -> (on_reject)')
        self.done(self.Rejected)


class DeleteDialog(QDialog, Ui_DeleteDialog):
    Rejected, Accepted = range(0, 2)

    def __init__(self):
        QDialog.__init__(self)
        Lumberjack.info('spawning a << DeleteDialog >>')
        self.setupUi(self)

        style.set_window_style(self)

        self.buttonBox.addButton('Delete', QDialogButtonBox.AcceptRole)
        button_list = self.buttonBox.buttons()
        for button in button_list:
            button.setFocusPolicy(Qt.NoFocus)

        self.buttonBox.rejected.connect(self.on_reject)
        self.buttonBox.accepted.connect(self.on_accept)

    def on_accept(self):
        Lumberjack.info('< DeleteDialog > - -> (on_accept)')
        self.done(self.Accepted)

    def on_reject(self):
        Lumberjack.info('< DeleteDialog > - -> (on_reject)')
        self.done(self.Rejected)


class TerminationDialog(QDialog, Ui_TerminationDialog):

    def __init__(self):
        QDialog.__init__(self)
        Lumberjack.info('spawning a << TerminationDialog >>')
        self.setupUi(self)

        style.set_window_style(self)

        errorIcon = qta.icon('fa.times-circle', color='#FF1744')
        errorPixmap = errorIcon.pixmap(50, 50)
        self.iconContainer.setPixmap(errorPixmap)

        self.buttonBox.accepted.connect(self.on_accept)
        self.buttonBox.rejected.connect(self.on_reject)

    def on_accept(self):
        Lumberjack.info('< TerminationDialog > - -> (on_accept)')
        self.done(0)

    def on_reject(self):
        Lumberjack.info('< TerminationDialog > - -> (on_reject)')
        self.done(0)
