# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\bank_account_form.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BankAccountFormInsert(object):
    def setupUi(self, BankAccountFormInsert):
        BankAccountFormInsert.setObjectName("BankAccountFormInsert")
        BankAccountFormInsert.resize(286, 273)
        self.formLayout = QtWidgets.QFormLayout(BankAccountFormInsert)
        self.formLayout.setObjectName("formLayout")
        self.bankNameLabel = QtWidgets.QLabel(BankAccountFormInsert)
        self.bankNameLabel.setObjectName("bankNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.bankNameLabel)
        self.bankNameLineEdit = QtWidgets.QLineEdit(BankAccountFormInsert)
        self.bankNameLineEdit.setObjectName("bankNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bankNameLineEdit)
        self.UserLabel = QtWidgets.QLabel(BankAccountFormInsert)
        self.UserLabel.setObjectName("UserLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.UserLabel)
        self.userComboBox = MyComboBox(BankAccountFormInsert)
        self.userComboBox.setObjectName("userComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.userComboBox)
        self.accountLabel = QtWidgets.QLabel(BankAccountFormInsert)
        self.accountLabel.setObjectName("accountLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.accountLabel)
        self.accountLineEdit = QtWidgets.QLineEdit(BankAccountFormInsert)
        self.accountLineEdit.setToolTip("")
        self.accountLineEdit.setStatusTip("")
        self.accountLineEdit.setAccessibleDescription("")
        self.accountLineEdit.setObjectName("accountLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.accountLineEdit)
        self.balanceLabel = QtWidgets.QLabel(BankAccountFormInsert)
        self.balanceLabel.setObjectName("balanceLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.balanceLabel)
        self.balanceCurrencyEdit = MyCurrencyBox(BankAccountFormInsert)
        self.balanceCurrencyEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.balanceCurrencyEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.balanceCurrencyEdit.setObjectName("balanceCurrencyEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.balanceCurrencyEdit)

        self.retranslateUi(BankAccountFormInsert)
        QtCore.QMetaObject.connectSlotsByName(BankAccountFormInsert)

    def retranslateUi(self, BankAccountFormInsert):
        _translate = QtCore.QCoreApplication.translate
        BankAccountFormInsert.setWindowTitle(_translate("BankAccountFormInsert", "Form"))
        self.bankNameLabel.setText(_translate("BankAccountFormInsert", "Bank name"))
        self.UserLabel.setText(_translate("BankAccountFormInsert", "User"))
        self.accountLabel.setText(_translate("BankAccountFormInsert", "Account Nr."))
        self.balanceLabel.setText(_translate("BankAccountFormInsert", "Balance"))

from MyQtness.myWidgets import MyComboBox, MyCurrencyBox
