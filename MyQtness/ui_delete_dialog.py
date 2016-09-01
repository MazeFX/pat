# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\delete_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeleteDialog(object):
    def setupUi(self, DeleteDialog):
        DeleteDialog.setObjectName("DeleteDialog")
        DeleteDialog.resize(427, 133)
        self.verticalLayout = QtWidgets.QVBoxLayout(DeleteDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TextLabel = QtWidgets.QLabel(DeleteDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TextLabel.setFont(font)
        self.TextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TextLabel.setObjectName("TextLabel")
        self.verticalLayout.addWidget(self.TextLabel)
        self.buttonBox = QtWidgets.QDialogButtonBox(DeleteDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DeleteDialog)
        QtCore.QMetaObject.connectSlotsByName(DeleteDialog)

    def retranslateUi(self, DeleteDialog):
        _translate = QtCore.QCoreApplication.translate
        DeleteDialog.setWindowTitle(_translate("DeleteDialog", "Delete"))
        self.TextLabel.setText(_translate("DeleteDialog", "Are you sure you want to delete selected item?"))

