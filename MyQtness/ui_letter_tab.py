# -*- coding: utf-8 -*-

# form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\letter_tab.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("form")
        Form.resize(820, 597)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setDragEnabled(False)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.horizontalHeader().setSortIndicatorShown(True)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setHighlightSections(False)
        self.horizontalLayout.addWidget(self.tableView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("form", "form"))

