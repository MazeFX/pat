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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuPAT = QtWidgets.QMenu(self.menubar)
        self.menuPAT.setObjectName("menuPAT")
        self.menuLetter = QtWidgets.QMenu(self.menubar)
        self.menuLetter.setObjectName("menuLetter")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAddLetter = QtWidgets.QAction(MainWindow)
        self.actionAddLetter.setObjectName("actionAddLetter")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuLetter.addAction(self.actionAddLetter)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuPAT.menuAction())
        self.menubar.addAction(self.menuLetter.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PAT - The Personal Admin Tool"))
        self.menuPAT.setTitle(_translate("MainWindow", "PAT"))
        self.menuLetter.setTitle(_translate("MainWindow", "Letter"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAddLetter.setText(_translate("MainWindow", "Add"))
        self.actionAddLetter.setToolTip(_translate("MainWindow", "Add new letter"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

