# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\email_address_form.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EmailAddressFormInsert(object):
    def setupUi(self, EmailAddressFormInsert):
        EmailAddressFormInsert.setObjectName("EmailAddressFormInsert")
        EmailAddressFormInsert.resize(286, 273)
        self.formLayout = QtWidgets.QFormLayout(EmailAddressFormInsert)
        self.formLayout.setObjectName("formLayout")
        self.userLabel = QtWidgets.QLabel(EmailAddressFormInsert)
        self.userLabel.setObjectName("userLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.userLabel)
        self.userComboBox = MyComboBox(EmailAddressFormInsert)
        self.userComboBox.setObjectName("userComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.userComboBox)
        self.addressLabel = QtWidgets.QLabel(EmailAddressFormInsert)
        self.addressLabel.setObjectName("addressLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.addressLabel)
        self.addressLineEdit = QtWidgets.QLineEdit(EmailAddressFormInsert)
        self.addressLineEdit.setToolTip("")
        self.addressLineEdit.setStatusTip("")
        self.addressLineEdit.setAccessibleDescription("")
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.addressLineEdit)

        self.retranslateUi(EmailAddressFormInsert)
        QtCore.QMetaObject.connectSlotsByName(EmailAddressFormInsert)

    def retranslateUi(self, EmailAddressFormInsert):
        _translate = QtCore.QCoreApplication.translate
        EmailAddressFormInsert.setWindowTitle(_translate("EmailAddressFormInsert", "Form"))
        self.userLabel.setText(_translate("EmailAddressFormInsert", "User"))
        self.addressLabel.setText(_translate("EmailAddressFormInsert", "Email address"))

from MyQtness.myWidgets import MyComboBox
