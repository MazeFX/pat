# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\basic_form.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RelationForm(object):
    def setupUi(self, RelationForm):
        RelationForm.setObjectName("RelationForm")
        RelationForm.resize(320, 559)
        RelationForm.setMaximumSize(QtCore.QSize(350, 16777215))
        RelationForm.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(RelationForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(RelationForm)
        self.titleLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonAdd = QtWidgets.QPushButton(RelationForm)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayout_2.addWidget(self.pushButtonAdd)
        self.pushButtonEdit = QtWidgets.QPushButton(RelationForm)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.horizontalLayout_2.addWidget(self.pushButtonEdit)
        self.pushButtonDelete = QtWidgets.QPushButton(RelationForm)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout_2.addWidget(self.pushButtonDelete)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(RelationForm)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem = QtWidgets.QSpacerItem(40, 50, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonSave = QtWidgets.QPushButton(RelationForm)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.pushButtonReset = QtWidgets.QPushButton(RelationForm)
        self.pushButtonReset.setObjectName("pushButtonReset")
        self.horizontalLayout.addWidget(self.pushButtonReset)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(RelationForm)
        QtCore.QMetaObject.connectSlotsByName(RelationForm)

    def retranslateUi(self, RelationForm):
        _translate = QtCore.QCoreApplication.translate
        RelationForm.setWindowTitle(_translate("RelationForm", "Form"))
        self.titleLabel.setText(_translate("RelationForm", "Title"))
        self.pushButtonAdd.setText(_translate("RelationForm", "Add new"))
        self.pushButtonEdit.setText(_translate("RelationForm", "Edit"))
        self.pushButtonDelete.setText(_translate("RelationForm", "Delete"))
        self.pushButtonSave.setText(_translate("RelationForm", "Save"))
        self.pushButtonReset.setText(_translate("RelationForm", "Reset"))

