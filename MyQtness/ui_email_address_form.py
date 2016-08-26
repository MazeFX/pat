# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\email_address_form.ui'
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
        self.UserLabel = QtWidgets.QLabel(LetterFormInsert)
        self.UserLabel.setObjectName("UserLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.UserLabel)
        self.userComboBox = MyComboBox(LetterFormInsert)
        self.userComboBox.setObjectName("userComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.userComboBox)
        self.addressLabel = QtWidgets.QLabel(LetterFormInsert)
        self.addressLabel.setObjectName("addressLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.addressLabel)
        self.emailAddressLineEdit = QtWidgets.QLineEdit(LetterFormInsert)
        self.emailAddressLineEdit.setToolTip("")
        self.emailAddressLineEdit.setStatusTip("")
        self.emailAddressLineEdit.setAccessibleDescription("")
        self.emailAddressLineEdit.setObjectName("emailAddressLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.emailAddressLineEdit)

        self.retranslateUi(LetterFormInsert)
        QtCore.QMetaObject.connectSlotsByName(LetterFormInsert)

    def retranslateUi(self, LetterFormInsert):
        _translate = QtCore.QCoreApplication.translate
        LetterFormInsert.setWindowTitle(_translate("LetterFormInsert", "Form"))
        self.UserLabel.setText(_translate("LetterFormInsert", "User"))
        self.addressLabel.setText(_translate("LetterFormInsert", "Email address"))

from MyQtness.myWidgets import MyComboBox
