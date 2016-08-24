# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\letter_form.ui'
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
        self.dateLabel = QtWidgets.QLabel(LetterFormInsert)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dateLabel)
        self.dateDateEdit = QtWidgets.QDateEdit(LetterFormInsert)
        self.dateDateEdit.setEnabled(True)
        self.dateDateEdit.setWrapping(False)
        self.dateDateEdit.setFrame(True)
        self.dateDateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 7, 6), QtCore.QTime(0, 0, 0)))
        self.dateDateEdit.setCalendarPopup(True)
        self.dateDateEdit.setDate(QtCore.QDate(2016, 7, 6))
        self.dateDateEdit.setObjectName("dateDateEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateDateEdit)
        self.subjectLabel = QtWidgets.QLabel(LetterFormInsert)
        self.subjectLabel.setObjectName("subjectLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.subjectLabel)
        self.subjectLineEdit = QtWidgets.QLineEdit(LetterFormInsert)
        self.subjectLineEdit.setObjectName("subjectLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.subjectLineEdit)
        self.UserLabel = QtWidgets.QLabel(LetterFormInsert)
        self.UserLabel.setObjectName("UserLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.UserLabel)
        self.userComboBox = MyComboBox(LetterFormInsert)
        self.userComboBox.setObjectName("userComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.userComboBox)
        self.senderLabel = QtWidgets.QLabel(LetterFormInsert)
        self.senderLabel.setObjectName("senderLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.senderLabel)
        self.senderComboBox = MyComboBox(LetterFormInsert)
        self.senderComboBox.setObjectName("senderComboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.senderComboBox)
        self.referenceLabel = QtWidgets.QLabel(LetterFormInsert)
        self.referenceLabel.setObjectName("referenceLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.referenceLabel)
        self.referenceLineEdit = QtWidgets.QLineEdit(LetterFormInsert)
        self.referenceLineEdit.setToolTip("")
        self.referenceLineEdit.setStatusTip("")
        self.referenceLineEdit.setAccessibleDescription("")
        self.referenceLineEdit.setObjectName("referenceLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.referenceLineEdit)
        self.scanLabel = QtWidgets.QLabel(LetterFormInsert)
        self.scanLabel.setObjectName("scanLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.scanLabel)
        self.scanFileDrop = MyDragDropBox(LetterFormInsert)
        self.scanFileDrop.setMinimumSize(QtCore.QSize(0, 100))
        self.scanFileDrop.setAcceptDrops(True)
        self.scanFileDrop.setAutoFillBackground(False)
        self.scanFileDrop.setStyleSheet("")
        self.scanFileDrop.setObjectName("scanFileDrop")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.scanFileDrop)

        self.retranslateUi(LetterFormInsert)
        QtCore.QMetaObject.connectSlotsByName(LetterFormInsert)

    def retranslateUi(self, LetterFormInsert):
        _translate = QtCore.QCoreApplication.translate
        LetterFormInsert.setWindowTitle(_translate("LetterFormInsert", "Form"))
        self.dateLabel.setText(_translate("LetterFormInsert", "Date"))
        self.subjectLabel.setText(_translate("LetterFormInsert", "Subject"))
        self.UserLabel.setText(_translate("LetterFormInsert", "Adressed User"))
        self.senderLabel.setText(_translate("LetterFormInsert", "Sender"))
        self.referenceLabel.setText(_translate("LetterFormInsert", "Reference"))
        self.scanLabel.setText(_translate("LetterFormInsert", "Scan"))

from MyQtness.myWidgets import MyComboBox, MyDragDropBox
