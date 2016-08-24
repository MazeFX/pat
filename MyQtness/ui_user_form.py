# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\user_form.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UserFormInsert(object):
    def setupUi(self, UserFormInsert):
        UserFormInsert.setObjectName("UserFormInsert")
        UserFormInsert.resize(286, 273)
        self.formLayout = QtWidgets.QFormLayout(UserFormInsert)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(UserFormInsert)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(UserFormInsert)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.fullnameLabel = QtWidgets.QLabel(UserFormInsert)
        self.fullnameLabel.setObjectName("fullnameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fullnameLabel)
        self.fullnameLineEdit = QtWidgets.QLineEdit(UserFormInsert)
        self.fullnameLineEdit.setToolTip("")
        self.fullnameLineEdit.setStatusTip("")
        self.fullnameLineEdit.setAccessibleDescription("")
        self.fullnameLineEdit.setObjectName("fullnameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fullnameLineEdit)
        self.passwordLabel = QtWidgets.QLabel(UserFormInsert)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(UserFormInsert)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)

        self.retranslateUi(UserFormInsert)
        QtCore.QMetaObject.connectSlotsByName(UserFormInsert)

    def retranslateUi(self, UserFormInsert):
        _translate = QtCore.QCoreApplication.translate
        UserFormInsert.setWindowTitle(_translate("UserFormInsert", "Form"))
        self.nameLabel.setText(_translate("UserFormInsert", "Name"))
        self.fullnameLabel.setText(_translate("UserFormInsert", "Full Name"))
        self.passwordLabel.setText(_translate("UserFormInsert", "Password"))

