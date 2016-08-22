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
from PyQt5.QtCore import QCoreApplication, QSettings, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QLabel, QTabWidget, QSystemTrayIcon
import qtawesome as qta
from colorama import Fore, Back, Style
from colorama import init as colorama

from dialogs import LoginDialog, SettingsDialog, CloseDialog
from MyQtness.ui_main_window import Ui_MainWindow
from MyQtness import style
from tabs import LetterListTab, UserListTab, RelationListTab, HomeTab
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

        self.menubar.setFocusPolicy(Qt.NoFocus)
        envelopeIcon = qta.icon('fa.envelope', color='white')
        self.actionListLetters.setIcon(envelopeIcon)
        relationIcon = qta.icon('fa.group', color='white')
        self.actionListRelations.setIcon(relationIcon)
        userIcon = qta.icon('fa.user', color='white')
        self.actionListUsers.setIcon(userIcon)
        wrenchIcon = qta.icon('fa.wrench', color='white')
        self.actionSettings.setIcon(wrenchIcon)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_home = HomeTab()
        self.tab_list.append(self.tab_home)
        self.tab_home.dbhelper = self.dbhelper
        self.tab_home.setObjectName("tab_home")
        icon = qta.icon('fa.home', color='white')
        self.tabWidget.addTab(self.tab_home, icon, self._translate("MainWindow", "Home"))
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
        self.trayIcon.showMessage('PAT Service', 'PAT service is now running..')

    def _retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_home), self._translate("MainWindow", "Home"))

    def show_list(self, *args):
        print(Fore.MAGENTA + '$! Showing the list called with args: ', args)
        action_text = args[0].text()
        icon = args[0].icon()
        print(Fore.MAGENTA + '$! Action text received: ', action_text)
        if action_text == 'Letters':
            print(Fore.MAGENTA + '$! Opening Letter List tab..')
            self.add_tab(LetterListTab, 'Letters', icon)
        if action_text == 'Users':
            print(Fore.MAGENTA + '$! Opening User List tab..')
            self.add_tab(UserListTab, 'Users', icon)
        if action_text == 'Relations':
            print(Fore.MAGENTA + '$! Opening Relation List tab..')
            self.add_tab(RelationListTab, 'Relations', icon)

    def add_tab(self, tab_cls, tab_name, icon):
        new_tab = tab_cls(self.dbhelper)
        print(Fore.MAGENTA + 'Adding a tab with class: ', str(tab_cls))
        new_tab.setObjectName(str(tab_cls))
        self.tabWidget.addTab(new_tab, icon, self._translate("MainWindow", tab_name))

        print(Fore.MAGENTA + 'New tab added to tab list.')
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(new_tab))
        self.tab_list.append(new_tab)

    def handle_tray_event(self, *args):
        print(Fore.MAGENTA + '$! Received a tray action with args: ', args)
        if args[0] == 3:
            self.show()
        # TODO - create condition for other menu actions

    def add_letter(self):
        print(Fore.MAGENTA + 'signal recieved for action add letter.')
        self.tab_letter = LetterListTab(self.dbhelper)
        print(Fore.MAGENTA + 'Letterform initialized.')
        self.tab_letter.setObjectName("tab_letter")
        self.tabWidget.addTab(self.tab_letter, "")
        print(Fore.MAGENTA + 'Letterform added to mainwindow.')
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_letter), self._translate("MainWindow", "Letters"))
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.tab_letter))

    def close_tab(self, index):
        requesting_tab = self.tab_list[index]
        print(Fore.MAGENTA + 'requesting tab is: ', requesting_tab)
        if requesting_tab.form.edit_mode:
            print(Fore.MAGENTA + 'Tab is in edit mode.')
            requesting_tab.form.toggle_edit_mode(False, None, None)
        if requesting_tab.form.edit_mode is None:
            print(Fore.MAGENTA + 'Tab is now in equil.')
        self.tabWidget.removeTab(index)
        del self.tab_list[index]

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
        print(Fore.MAGENTA + "User has clicked the red x on the main window")
        # TODO - On close check for unsaved changes

        close_dialog = CloseDialog()
        result = close_dialog.exec_()
        if result == close_dialog.Minimize:
            self.hide()
            event.ignore()
        elif result == close_dialog.Rejected:
            event.ignore()
        elif result == close_dialog.Exit:
            print(Fore.MAGENTA + "Exiting via save dialog, result = ", result)
            self.trayIcon.hide()
            event.accept()


if __name__ == "__main__":
    visible = True
    colorama(autoreset=True)
    app = QApplication(sys.argv)
    app.setApplicationName('PAT')
    app.setOrganizationName("MazeFX Solutions")
    app.setOrganizationDomain("MazeFX.pythonanywhere.com")

    QFontDatabase().addApplicationFont("C:\PDE\projects\qt\pat\MyQtness\style\ethnocentric.ttf")
    QFontDatabase().addApplicationFont("C:\PDE\projects\qt\pat\MyQtness\style/ubuntu_bold.ttf")

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
