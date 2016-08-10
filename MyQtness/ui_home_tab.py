# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\home_tab.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HomeTab(object):
    def setupUi(self, HomeTab):
        HomeTab.setObjectName("HomeTab")
        HomeTab.resize(951, 714)
        self.verticalLayout = QtWidgets.QVBoxLayout(HomeTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header1 = QtWidgets.QLabel(HomeTab)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.Header1.setFont(font)
        self.Header1.setObjectName("Header1")
        self.verticalLayout.addWidget(self.Header1)
        self.Header2 = QtWidgets.QLabel(HomeTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Header2.setFont(font)
        self.Header2.setObjectName("Header2")
        self.verticalLayout.addWidget(self.Header2)
        spacerItem = QtWidgets.QSpacerItem(40, 550, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(HomeTab)
        QtCore.QMetaObject.connectSlotsByName(HomeTab)

    def retranslateUi(self, HomeTab):
        _translate = QtCore.QCoreApplication.translate
        HomeTab.setWindowTitle(_translate("HomeTab", "Form"))
        self.Header1.setText(_translate("HomeTab", "P.A.T."))
        self.Header2.setText(_translate("HomeTab", "Personal Admin Tool"))

