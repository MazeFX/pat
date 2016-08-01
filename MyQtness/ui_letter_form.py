# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'letter_form.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_letter_form(object):
    def setupUi(self, letter_form):
        letter_form.setObjectName("letter_form")
        letter_form.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(letter_form)
        self.centralWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.centralWidget.setObjectName("centralWidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralWidget)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.letter_sender_input = QtWidgets.QLineEdit(self.centralWidget)
        self.letter_sender_input.setObjectName("letter_sender_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.letter_sender_input)
        self.label_sender = QtWidgets.QLabel(self.centralWidget)
        self.label_sender.setObjectName("label_sender")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_sender)
        self.label_date = QtWidgets.QLabel(self.centralWidget)
        self.label_date.setObjectName("label_date")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_date)
        self.letter_date_input = QtWidgets.QDateEdit(self.centralWidget)
        self.letter_date_input.setAlignment(QtCore.Qt.AlignCenter)
        self.letter_date_input.setDate(QtCore.QDate(2016, 1, 1))
        self.letter_date_input.setObjectName("letter_date_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.letter_date_input)
        letter_form.setCentralWidget(self.centralWidget)

        self.retranslateUi(letter_form)
        QtCore.QMetaObject.connectSlotsByName(letter_form)

    def retranslateUi(self, letter_form):
        _translate = QtCore.QCoreApplication.translate
        letter_form.setWindowTitle(_translate("letter_form", "letter_form"))
        self.label_sender.setText(_translate("letter_form", "Sender"))
        self.label_date.setText(_translate("letter_form", "Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    letter_form = QtWidgets.QMainWindow()
    ui = Ui_letter_form()
    ui.setupUi(letter_form)
    letter_form.show()
    sys.exit(app.exec_())

