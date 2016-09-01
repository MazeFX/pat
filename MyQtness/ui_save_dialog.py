# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\save_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SaveDialog(object):
    def setupUi(self, SaveDialog):
        SaveDialog.setObjectName("SaveDialog")
        SaveDialog.resize(427, 133)
        self.verticalLayout = QtWidgets.QVBoxLayout(SaveDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TextLabel = QtWidgets.QLabel(SaveDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TextLabel.setFont(font)
        self.TextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TextLabel.setObjectName("TextLabel")
        self.verticalLayout.addWidget(self.TextLabel)
        self.buttonBox = QtWidgets.QDialogButtonBox(SaveDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SaveDialog)
        self.buttonBox.accepted.connect(SaveDialog.accept)
        self.buttonBox.rejected.connect(SaveDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SaveDialog)

    def retranslateUi(self, SaveDialog):
        _translate = QtCore.QCoreApplication.translate
        SaveDialog.setWindowTitle(_translate("SaveDialog", "Save changes"))
        self.TextLabel.setText(_translate("SaveDialog", "You have unsaved changes, what do you want to do?"))

