# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuPAT = QtWidgets.QMenu(self.menubar)
        self.menuPAT.setObjectName("menuPAT")
        self.menuLists = QtWidgets.QMenu(self.menubar)
        self.menuLists.setGeometry(QtCore.QRect(381, 116, 159, 126))
        self.menuLists.setObjectName("menuLists")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionListLetters = QtWidgets.QAction(MainWindow)
        self.actionListLetters.setObjectName("actionListLetters")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionListUsers = QtWidgets.QAction(MainWindow)
        self.actionListUsers.setObjectName("actionListUsers")
        self.actionListRelations = QtWidgets.QAction(MainWindow)
        self.actionListRelations.setObjectName("actionListRelations")
        self.menuPAT.addAction(self.actionSettings)
        self.menuLists.addAction(self.actionListUsers)
        self.menuLists.addAction(self.actionListLetters)
        self.menuLists.addAction(self.actionListRelations)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuPAT.menuAction())
        self.menubar.addAction(self.menuLists.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PAT - The Personal Admin Tool"))
        self.menuPAT.setTitle(_translate("MainWindow", "PAT"))
        self.menuLists.setTitle(_translate("MainWindow", "Lists"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionListLetters.setText(_translate("MainWindow", "Letters"))
        self.actionListLetters.setToolTip(_translate("MainWindow", "List of letters"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionListUsers.setText(_translate("MainWindow", "Users"))
        self.actionListUsers.setToolTip(_translate("MainWindow", "List of Users"))
        self.actionListRelations.setText(_translate("MainWindow", "Relations"))
        self.actionListRelations.setToolTip(_translate("MainWindow", "List of Relations"))

