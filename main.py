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
from PyQt5.QtGui import QFontDatabase, QIcon
from PyQt5.QtCore import QCoreApplication, QSettings
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QLabel, QTabWidget, QSystemTrayIcon
from colorama import Fore, Back, Style
from colorama import init as colorama

from dialogs import LoginDialog, SettingsDialog
from MyQtness.ui_main_window import Ui_MainWindow
from MyQtness import style
from tabs import LetterTab, HomeTab
from db.helper import DbHelper


class MainApp(QMainWindow, Ui_MainWindow):

    _translate = QCoreApplication.translate
    tab_list = []
    # TODO - add dutch translation files

    def __init__(self, *args):
        super(MainApp, self).__init__(*args)
        self.load_settings()
        self.setup_tray()
        self.dbhelper = DbHelper()

        self.setupUi(self)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_home = HomeTab()
        self.tab_list.append(self.tab_home)
        self.tab_home.dbhelper = self.dbhelper
        self.tab_home.setObjectName("tab_home")
        self.tabWidget.addTab(self.tab_home, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self._retranslateUi(self)
        self.actionSettings.triggered.connect(self.show_settings)
        self.menuLists.triggered.connect(self.show_list)
        self.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.setWindowIcon(QIcon(':/app_icons/rc/tray_icon.png'))
        builderLabel = QLabel('made by: MazeFX Solutions')
        self.statusbar.addPermanentWidget(builderLabel)

    def setup_tray(self):
        self.trayIcon = QSystemTrayIcon(QIcon(':/app_icons/rc/tray_icon.png'), self)
        self.trayMenu = QMenu(self)
        showAction = self.trayMenu.addAction("Open PAT")
        self.trayMenu.addSeparator()
        exitAction = self.trayMenu.addAction("Exit")
        self.trayIcon.setContextMenu(self.trayMenu)
        self.trayMenu.triggered.connect(self.handle_tray_event)
        self.trayIcon.activated.connect(self.handle_tray_event)
        self.trayIcon.show()
        self.trayIcon.showMessage('PAT Service', 'PAT service is no running..')

    def _retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_home), self._translate("MainWindow", "Home"))

    def show_list(self, *args):
        print(Fore.MAGENTA + '$! Showing the list called with args: ', args)

    def handle_tray_event(self, *args):
        print(Fore.MAGENTA + '$! Received a tray action with args: ', args)
        if args[0] == 3:
            self.show()

    def add_letter(self):
        print(Fore.MAGENTA + 'signal recieved for action add letter.')
        self.tab_letter = LetterTab(self.dbhelper)
        print(Fore.MAGENTA + 'Letterform initialized.')
        self.tab_letter.setObjectName("tab_letter")
        self.tabWidget.addTab(self.tab_letter, "")
        print(Fore.MAGENTA + 'Letterform added to mainwindow.')
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_letter), self._translate("MainWindow", "Letters"))
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tab_letter))

    def close_tab(self, index):
        self.tabWidget.removeTab(index)

    def load_settings(self):
        self.settings = QSettings()
        int_value = self.settings.value('db_type', type=int)

        # TODO - possible setting for style setting
        stylesheet = style.load_stylesheet_pyqt5()
        self.setStyleSheet(stylesheet)
        print(Fore.MAGENTA + "load choosen database setting: %s" % repr(int_value))

    def show_settings(self):
        print(Fore.MAGENTA + 'Showing the Settings Dialog..')

        settings_dialog = SettingsDialog()
        settings_dialog.exec_()

    def closeEvent(self, event):
        print("User has clicked the red x on the main window")
        event.accept()



if __name__ == "__main__":
    visible = True
    colorama(autoreset=True)
    app = QApplication(sys.argv)
    app.setApplicationName('PAT')
    app.setOrganizationName("MazeFX Solutions")
    app.setOrganizationDomain("MazeFX.pythonanywhere.com")


    QFontDatabase().addApplicationFont("C:\PDE\projects\qt\pat\MyQtness\style\ethnocentric.ttf")
    Id = QFontDatabase().addApplicationFont("C:\PDE\projects\qt\pat\MyQtness\style/ubuntu_bold.ttf")

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
    for arg in sys.argv:
        if 'only-tray' in arg:
            visible = False

    if visible:
        w.show()
    app.exec_()
    sys.exit(-1)
