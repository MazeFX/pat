# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\user_form.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UserForm(object):
    def setupUi(self, UserForm):
        UserForm.setObjectName("UserForm")
        UserForm.resize(320, 559)
        UserForm.setMaximumSize(QtCore.QSize(350, 16777215))
        UserForm.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(UserForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleLabel = QtWidgets.QLabel(UserForm)
        self.TitleLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout.addWidget(self.TitleLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonAdd = QtWidgets.QPushButton(UserForm)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayout_2.addWidget(self.pushButtonAdd)
        self.pushButtonEdit = QtWidgets.QPushButton(UserForm)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.horizontalLayout_2.addWidget(self.pushButtonEdit)
        self.pushButtonDelete = QtWidgets.QPushButton(UserForm)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout_2.addWidget(self.pushButtonDelete)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(UserForm)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, -1, 0, -1)
        self.formLayout.setSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(UserForm)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(UserForm)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.fullnameLabel = QtWidgets.QLabel(UserForm)
        self.fullnameLabel.setObjectName("fullnameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fullnameLabel)
        self.fullnameLineEdit = QtWidgets.QLineEdit(UserForm)
        self.fullnameLineEdit.setToolTip("")
        self.fullnameLineEdit.setStatusTip("")
        self.fullnameLineEdit.setAccessibleDescription("")
        self.fullnameLineEdit.setObjectName("fullnameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fullnameLineEdit)
        self.passwordLabel = QtWidgets.QLabel(UserForm)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(UserForm)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonSave = QtWidgets.QPushButton(UserForm)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.pushButtonReset = QtWidgets.QPushButton(UserForm)
        self.pushButtonReset.setObjectName("pushButtonReset")
        self.horizontalLayout.addWidget(self.pushButtonReset)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(UserForm)
        QtCore.QMetaObject.connectSlotsByName(UserForm)

    def retranslateUi(self, UserForm):
        _translate = QtCore.QCoreApplication.translate
        UserForm.setWindowTitle(_translate("UserForm", "Form"))
        self.TitleLabel.setText(_translate("UserForm", "Users"))
        self.pushButtonAdd.setText(_translate("UserForm", "Add new"))
        self.pushButtonEdit.setText(_translate("UserForm", "Edit"))
        self.pushButtonDelete.setText(_translate("UserForm", "Delete"))
        self.nameLabel.setText(_translate("UserForm", "Name"))
        self.fullnameLabel.setText(_translate("UserForm", "Full Name"))
        self.passwordLabel.setText(_translate("UserForm", "Password"))
        self.pushButtonSave.setText(_translate("UserForm", "Save"))
        self.pushButtonReset.setText(_translate("UserForm", "Reset"))
