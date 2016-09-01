# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\termination_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TerminationDialog(object):
    def setupUi(self, TerminationDialog):
        TerminationDialog.setObjectName("TerminationDialog")
        TerminationDialog.resize(400, 192)
        self.verticalLayout = QtWidgets.QVBoxLayout(TerminationDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.iconContainer = QtWidgets.QLabel(TerminationDialog)
        self.iconContainer.setText("")
        self.iconContainer.setObjectName("iconContainer")
        self.horizontalLayout.addWidget(self.iconContainer)
        self.label = QtWidgets.QLabel(TerminationDialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(TerminationDialog)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(TerminationDialog)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(TerminationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(TerminationDialog)
        self.buttonBox.accepted.connect(TerminationDialog.accept)
        self.buttonBox.rejected.connect(TerminationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TerminationDialog)

    def retranslateUi(self, TerminationDialog):
        _translate = QtCore.QCoreApplication.translate
        TerminationDialog.setWindowTitle(_translate("TerminationDialog", "Error encountered!"))
        self.label.setText(_translate("TerminationDialog", "The application has encountered a serious error!"))
        self.label_2.setText(_translate("TerminationDialog", "Please contact your local administrator to address the situation. Please note time and date for referral to stored logfiles."))
        self.label_3.setText(_translate("TerminationDialog", "The application will now terminate to prevent damage to the database. It is then safe to restart."))

