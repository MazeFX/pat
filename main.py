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
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget

import qdarkstyle

from dialogs import LoginDialog
from forms import LetterForm
from MyQtness.ui_main_window import Ui_MainWindow


class MainApp(QMainWindow, Ui_MainWindow):
    _translate = QtCore.QCoreApplication.translate
    # TODO - add dutch translation files

    def __init__(self, *kwargs):
        super(MainApp, self).__init__(*kwargs)

        self.setupUi(self)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_home = QWidget()
        self.tab_home.setObjectName("tabHome")
        self.tabWidget.addTab(self.tab_home, "")

        self.verticalLayout.addWidget(self.tabWidget)

        # TODO  - Create own functions for loading the rc file, own style
        stylesheet = qdarkstyle.load_stylesheet_pyqt5()
        self.setStyleSheet(stylesheet)

        self._retranslateUi(self)
        self.actionAddLetter.triggered.connect(self.add_letter)
        self.tabWidget.tabCloseRequested.connect(self.close_tab)

    def _retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_home), self._translate("MainWindow", "Home"))

    def add_letter(self):
        print('signal recieved for action add letter.')
        self.tab_letter = LetterForm()
        print('Letterform initialized.')
        self.tab_letter.setObjectName("tab_letter")
        self.tabWidget.addTab(self.tab_letter, "")
        print('Letterform added to mainwindow.')
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_letter), self._translate("MainWindow", "Letters"))

    def close_tab(self, index):
        self.tabWidget.removeTab(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    loginDialog = LoginDialog()

    '''
    isAuth = False
    result = -1
    while not isAuth:
        result = loginDialog.exec_()

        if result == loginDialog.Success or result == LoginDialog.Rejected:
            isAuth = True

        else:
            isAuth = False

    if result == loginDialog.Success:
        '''
    w = MainApp()
    w.show()
    app.exec_()

    sys.exit(-1)
