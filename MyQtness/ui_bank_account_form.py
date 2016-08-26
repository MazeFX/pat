# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\bank_account_form.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LetterFormInsert(object):
    def setupUi(self, LetterFormInsert):
        LetterFormInsert.setObjectName("LetterFormInsert")
        LetterFormInsert.resize(286, 273)
        self.formLayout = QtWidgets.QFormLayout(LetterFormInsert)
        self.formLayout.setObjectName("formLayout")
        self.bankNameLabel = QtWidgets.QLabel(LetterFormInsert)
        self.bankNameLabel.setObjectName("bankNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.bankNameLabel)
        self.bankNameLineEdit = QtWidgets.QLineEdit(LetterFormInsert)
        self.bankNameLineEdit.setObjectName("bankNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bankNameLineEdit)
        self.UserLabel = QtWidgets.QLabel(LetterFormInsert)
        self.UserLabel.setObjectName("UserLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.UserLabel)
        self.userComboBox = MyComboBox(LetterFormInsert)
        self.userComboBox.setObjectName("userComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.userComboBox)
        self.accountLabel = QtWidgets.QLabel(LetterFormInsert)
        self.accountLabel.setObjectName("accountLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.accountLabel)
        self.accountLineEdit = QtWidgets.QLineEdit(LetterFormInsert)
        self.accountLineEdit.setToolTip("")
        self.accountLineEdit.setStatusTip("")
        self.accountLineEdit.setAccessibleDescription("")
        self.accountLineEdit.setObjectName("accountLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.accountLineEdit)
        self.balanceLabel = QtWidgets.QLabel(LetterFormInsert)
        self.balanceLabel.setObjectName("balanceLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.balanceLabel)
        self.balanceLineEdit = QtWidgets.QLineEdit(LetterFormInsert)
        self.balanceLineEdit.setObjectName("balanceLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.balanceLineEdit)

        self.retranslateUi(LetterFormInsert)
        QtCore.QMetaObject.connectSlotsByName(LetterFormInsert)

    def retranslateUi(self, LetterFormInsert):
        _translate = QtCore.QCoreApplication.translate
        LetterFormInsert.setWindowTitle(_translate("LetterFormInsert", "Form"))
        self.bankNameLabel.setText(_translate("LetterFormInsert", "Bank name"))
        self.UserLabel.setText(_translate("LetterFormInsert", "User"))
        self.accountLabel.setText(_translate("LetterFormInsert", "Account Nr."))
        self.balanceLabel.setText(_translate("LetterFormInsert", "Balance"))

from MyQtness.myWidgets import MyComboBox
