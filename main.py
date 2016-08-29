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

import logging
Lumberjack = logging.getLogger(__name__)

import os
import json
import sys

from PyQt5.QtGui import QFontDatabase, QIcon
from PyQt5.QtCore import QCoreApplication, QSettings, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QLabel, QTabWidget, QSystemTrayIcon
import qtawesome as qta
from colorama import Fore, Back, Style
from colorama import init as colorama

from dialogs import LoginDialog, SettingsDialog, CloseDialog, TerminationDialog
from MyQtness.ui_main_window import Ui_MainWindow
from MyQtness import style
from tabs import BankAccountListTab, ContractListTab, EmailAddressListTab, LetterListTab, \
    UserListTab, RelationListTab, TransactionListTab, HomeTab
from db.helper import DbHelper


class MainApp(QMainWindow, Ui_MainWindow):

    _translate = QCoreApplication.translate
    tab_list = []
    # TODO - add dutch translation files

    def __init__(self, isolated, *args):
        super(MainApp, self).__init__(*args)
        Lumberjack.info('spawning the <<< MainApp >>> hey says: I am the Main man here see!')
        self.load_settings()
        self.setup_tray(isolated)
        self.dbhelper = DbHelper()

        self.setupUi(self)
        self.iconize_controls()

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)

        self.actionSettings.triggered.connect(self.show_settings)
        self.menuPAT.triggered.connect(self.show_list)
        self.menuLists.triggered.connect(self.show_list)
        self.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.setWindowIcon(QIcon(':/app_icons/rc/PAT_icon.png'))
        builderLabel = QLabel('made by: MazeFX Solutions')
        self.statusbar.addPermanentWidget(builderLabel)
        self._retranslateUi(self)

    def iconize_controls(self):
        Lumberjack.info('< MainApp > - -> (iconize_controls)')

        homeIcon = qta.icon('fa.home', color='white')
        self.actionHome.setIcon(homeIcon)
        wrenchIcon = qta.icon('fa.wrench', color='white')
        self.actionSettings.setIcon(wrenchIcon)

        envelopeIcon = qta.icon('fa.envelope', color='white')
        self.actionListLetters.setIcon(envelopeIcon)
        relationIcon = qta.icon('fa.group', color='white')
        self.actionListRelations.setIcon(relationIcon)
        userIcon = qta.icon('fa.user', color='white')
        self.actionListUsers.setIcon(userIcon)

    def setup_tray(self, isolated):
        Lumberjack.info('< MainApp > - -> (setup_tray)')
        self.trayIcon = QSystemTrayIcon(QIcon(':/app_icons/rc/PAT_icon.png'), self)
        self.trayMenu = QMenu(self)
        showAction = self.trayMenu.addAction("Open PAT")
        self.trayMenu.addSeparator()
        exitAction = self.trayMenu.addAction("Exit")
        self.trayIcon.setContextMenu(self.trayMenu)
        self.trayMenu.triggered.connect(self.handle_tray_event)
        self.trayIcon.activated.connect(self.handle_tray_event)
        self.trayIcon.show()
        if isolated:
            self.trayIcon.showMessage('PAT Service', 'PAT service is now running..')

    def handle_tray_event(self, *args):
        Lumberjack.info('< MainApp > - -> (handle_tray_event)')
        print(Fore.MAGENTA + '$! Received a tray action with args: ', args)
        if args[0] == 3:
            self.show()
            return
        elif hasattr(args[0], 'text'):
            print(Fore.MAGENTA + '$! Tray event has text!!')
            if args[0].text() == 'Open PAT':
                self.show()
            elif args[0].text() == 'Exit':
                self.close()

    def _retranslateUi(self, MainWindow):
        pass

    def show_list(self, *args):
        Lumberjack.info('< MainApp > - -> (show_list)')
        Lumberjack.debug('(show_list) - args = ', args)

        action_text = args[0].text()
        icon = args[0].icon()

        Lumberjack.debug('(show_list) - Action text selector = ', action_text)
        print(Fore.MAGENTA + '$! Action text received: ', action_text)

        if action_text == 'Bank accounts':
            Lumberjack.info('< MainApp > >User action> : Adding Bank account List tab to self')
            self.add_tab(BankAccountListTab, 'Bank accounts', icon)

        if action_text == 'Contracts':
            Lumberjack.info('< MainApp > >User action> : Adding Contracts List tab to self')
            self.add_tab(ContractListTab, 'Contracts', icon)

        if action_text == 'Email addresses':
            Lumberjack.info('< MainApp > >User action> : Adding EmailAddress List tab to self')
            self.add_tab(EmailAddressListTab, 'Email addresses', icon)

        if action_text == 'Letters':
            Lumberjack.info('< MainApp > >User action> :  Adding Letter List tab to self')
            self.add_tab(LetterListTab, 'Letters', icon)

        if action_text == 'Users':
            Lumberjack.info('< MainApp > >User action> :  Adding User List tab to self')
            self.add_tab(UserListTab, 'Users', icon)

        if action_text == 'Relations':
            Lumberjack.info('< MainApp > >User action> :  Adding Relation List tab to self')
            self.add_tab(RelationListTab, 'Relations', icon)

        if action_text == 'Transactions':
            Lumberjack.info('< MainApp > >User action> :  Adding Transaction List tab to self')
            self.add_tab(TransactionListTab, 'Transactions', icon)

        if action_text == 'Home':
            Lumberjack.info('< MainApp > >User action> :  Adding Transaction List tab to self')
            self.add_tab(HomeTab, 'Home', icon)

    def show_home(self, *args):
        Lumberjack.info('< MainApp > - -> (show_home)')
        Lumberjack.debug('(show_home) - args = ', args)

    def show_settings(self):
        Lumberjack.info('< MainApp > - -> (show_settings)')
        settings_dialog = SettingsDialog()
        settings_dialog.exec_()

    def add_tab(self, tab_cls, tab_name, icon):
        Lumberjack.info('< MainApp > - -> (add_tab)')
        new_tab = tab_cls(self.dbhelper)
        print(Fore.MAGENTA + 'Adding a tab with class: ', str(tab_cls))
        new_tab.setObjectName(str(tab_cls))
        self.tabWidget.addTab(new_tab, icon, self._translate("MainWindow", tab_name))

        print(Fore.MAGENTA + 'New tab added to tab list.')
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(new_tab))
        self.tab_list.append(new_tab)

    def close_tab(self, index):
        # TODO - Check if index stays correct when moving tabs around
        requesting_tab = self.tab_list[index]
        print(Fore.MAGENTA + 'requesting tab is: ', requesting_tab)
        if hasattr(requesting_tab, 'form'):
            if requesting_tab.form.edit_mode:
                print(Fore.MAGENTA + 'Tab is in edit mode.')
                requesting_tab.form.toggle_edit_mode(False, None, None)
            if requesting_tab.form.edit_mode is None:
                print(Fore.MAGENTA + 'Tab is now in equil.')
                self.tabWidget.removeTab(index)
                del self.tab_list[index]
        else:
            self.tabWidget.removeTab(index)
            del self.tab_list[index]

    def load_settings(self):
        self.settings = QSettings()
        int_value = self.settings.value('db_type', type=int)

        # TODO - possible setting for style setting
        stylesheet = style.load_stylesheet_pyqt5()
        self.setStyleSheet(stylesheet)
        print(Fore.MAGENTA + "load choosen database setting: %s" % repr(int_value))

    def closeEvent(self, event):
        print(Fore.MAGENTA + "User has clicked the red x on the main window")
        for tab in self.tab_list:
            if hasattr(tab, 'form'):
                if tab.form.edit_mode:
                    print(Fore.MAGENTA + 'Tab is in edit mode.')
                    tab.form.toggle_edit_mode(False, None, None)

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


def setup_logging(
    default_path='lumberjack_config.json',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """

    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


if __name__ == "__main__":
    import logging.config
    colorama(autoreset=True)
    setup_logging()
    Lumberjack.info('=======================  Logger set up.. ')

    def my_excepthook(excType, excValue, traceback, logger=Lumberjack):
        logger.error("------  Logging an uncaught exception  ---------------------------->",
                     exc_info=(excType, excValue, traceback))
        termination_dialog = TerminationDialog()
        result = termination_dialog.exec_()
        if result == 0:
            Lumberjack.info('-->Trying to exit the app..')
            sys.exit(-1)
        Lumberjack.info('[result] = ', result)

    sys.excepthook = my_excepthook

    Lumberjack.info('=======================  Starting Application.. ')

    visible = True

    app = QApplication(sys.argv)
    app.setApplicationName('PAT')
    app.setOrganizationName("MazeFX Solutions")
    app.setOrganizationDomain("MazeFX.pythonanywhere.com")

    # TODO - Make font path relative
    QFontDatabase().addApplicationFont("C:\PDE\projects\qt\pat\MyQtness\style/fonts/ethnocentric.ttf")
    QFontDatabase().addApplicationFont("C:\PDE\projects\qt\pat\MyQtness\style/fonts/ubuntu_bold.ttf")

    # loginDialog = LoginDialog()
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
    for arg in sys.argv:
        if 'only-tray' in arg:
            isolated = True
        else:
            isolated = False

    w = MainApp(isolated)

    if not isolated:
        w.show()
    app.exec_()
    Lumberjack.info('=======================  Ending Application.. ')
    sys.exit(-1)


