# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\close_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CloseDialog(object):
    def setupUi(self, CloseDialog):
        CloseDialog.setObjectName("CloseDialog")
        CloseDialog.resize(427, 133)
        self.verticalLayout = QtWidgets.QVBoxLayout(CloseDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TextLabel = QtWidgets.QLabel(CloseDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TextLabel.setFont(font)
        self.TextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TextLabel.setObjectName("TextLabel")
        self.verticalLayout.addWidget(self.TextLabel)
        self.buttonBox = QtWidgets.QDialogButtonBox(CloseDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CloseDialog)
        QtCore.QMetaObject.connectSlotsByName(CloseDialog)

    def retranslateUi(self, CloseDialog):
        _translate = QtCore.QCoreApplication.translate
        CloseDialog.setWindowTitle(_translate("CloseDialog", "Dialog"))
        self.TextLabel.setText(_translate("CloseDialog", "<html><head/><body><p>You are about to close PAT.<br/>Do you want to exit or minimize to tray?</p></body></html>"))

