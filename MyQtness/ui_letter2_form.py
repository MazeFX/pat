# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\letter2_form.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LetterForm(object):
    def setupUi(self, LetterForm):
        LetterForm.setObjectName("LetterForm")
        LetterForm.resize(286, 273)
        self.formLayout = QtWidgets.QFormLayout(LetterForm)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(LetterForm)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(LetterForm)
        self.nameLineEdit.setToolTip("")
        self.nameLineEdit.setStatusTip("")
        self.nameLineEdit.setAccessibleDescription("")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.fullNameLabel = QtWidgets.QLabel(LetterForm)
        self.fullNameLabel.setObjectName("fullNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.fullNameLabel)
        self.fullNameLineEdit = QtWidgets.QLineEdit(LetterForm)
        self.fullNameLineEdit.setObjectName("fullNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fullNameLineEdit)
        self.startDateLabel = QtWidgets.QLabel(LetterForm)
        self.startDateLabel.setObjectName("startDateLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.startDateLabel)
        self.startDateEdit = QtWidgets.QDateEdit(LetterForm)
        self.startDateEdit.setEnabled(True)
        self.startDateEdit.setWrapping(False)
        self.startDateEdit.setFrame(True)
        self.startDateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.startDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 7, 6), QtCore.QTime(0, 0, 0)))
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setDate(QtCore.QDate(2016, 7, 6))
        self.startDateEdit.setObjectName("startDateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.startDateEdit)
        self.endDateLabel = QtWidgets.QLabel(LetterForm)
        self.endDateLabel.setObjectName("endDateLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.endDateLabel)
        self.endDateEdit = QtWidgets.QDateEdit(LetterForm)
        self.endDateEdit.setEnabled(True)
        self.endDateEdit.setWrapping(False)
        self.endDateEdit.setFrame(True)
        self.endDateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.endDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 7, 6), QtCore.QTime(0, 0, 0)))
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setDate(QtCore.QDate(2016, 7, 6))
        self.endDateEdit.setObjectName("endDateEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.endDateEdit)
        self.referenceLabel = QtWidgets.QLabel(LetterForm)
        self.referenceLabel.setObjectName("referenceLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.referenceLabel)
        self.referenceLineEdit = QtWidgets.QLineEdit(LetterForm)
        self.referenceLineEdit.setObjectName("referenceLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.referenceLineEdit)
        self.bankAccountLabel = QtWidgets.QLabel(LetterForm)
        self.bankAccountLabel.setObjectName("bankAccountLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.bankAccountLabel)
        self.bankAccountLineEdit = QtWidgets.QLineEdit(LetterForm)
        self.bankAccountLineEdit.setObjectName("bankAccountLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.bankAccountLineEdit)
        self.typeLabel = QtWidgets.QLabel(LetterForm)
        self.typeLabel.setObjectName("typeLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.typeLabel)
        self.typeComboBox = QtWidgets.QComboBox(LetterForm)
        self.typeComboBox.setObjectName("typeComboBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.typeComboBox)

        self.retranslateUi(LetterForm)
        QtCore.QMetaObject.connectSlotsByName(LetterForm)

    def retranslateUi(self, LetterForm):
        _translate = QtCore.QCoreApplication.translate
        LetterForm.setWindowTitle(_translate("LetterForm", "Form"))
        self.nameLabel.setText(_translate("LetterForm", "Name"))
        self.fullNameLabel.setText(_translate("LetterForm", "Full Name"))
        self.startDateLabel.setText(_translate("LetterForm", "Start date"))
        self.endDateLabel.setText(_translate("LetterForm", "End date"))
        self.referenceLabel.setText(_translate("LetterForm", "Reference"))
        self.bankAccountLabel.setText(_translate("LetterForm", "Bank account"))
        self.typeLabel.setText(_translate("LetterForm", "Relation type"))
