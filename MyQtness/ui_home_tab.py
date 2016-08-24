# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PDE\projects\qt\pat\MyQtness\ui\home_tab.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HomeTab(object):
    def setupUi(self, HomeTab):
        HomeTab.setObjectName("HomeTab")
        HomeTab.resize(951, 716)
        self.horizontalLayout = QtWidgets.QHBoxLayout(HomeTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Header1 = QtWidgets.QLabel(HomeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Header1.sizePolicy().hasHeightForWidth())
        self.Header1.setSizePolicy(sizePolicy)
        self.Header1.setAlignment(QtCore.Qt.AlignCenter)
        self.Header1.setObjectName("Header1")
        self.verticalLayout_3.addWidget(self.Header1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Header2_1 = QtWidgets.QLabel(HomeTab)
        self.Header2_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Header2_1.setObjectName("Header2_1")
        self.horizontalLayout_3.addWidget(self.Header2_1)
        self.Header2_2 = QtWidgets.QLabel(HomeTab)
        self.Header2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Header2_2.setObjectName("Header2_2")
        self.horizontalLayout_3.addWidget(self.Header2_2)
        self.Header2_3 = QtWidgets.QLabel(HomeTab)
        self.Header2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Header2_3.setObjectName("Header2_3")
        self.horizontalLayout_3.addWidget(self.Header2_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 300, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 30, 30, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pyClock = PyAnalogClock(HomeTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pyClock.sizePolicy().hasHeightForWidth())
        self.pyClock.setSizePolicy(sizePolicy)
        self.pyClock.setMinimumSize(QtCore.QSize(300, 300))
        self.pyClock.setStyleSheet("PyAnalogClock {\n"
"padding-right: 20px;\n"
"}")
        self.pyClock.setObjectName("pyClock")
        self.verticalLayout_2.addWidget(self.pyClock, 0, QtCore.Qt.AlignRight)
        spacerItem3 = QtWidgets.QSpacerItem(40, 250, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(HomeTab)
        QtCore.QMetaObject.connectSlotsByName(HomeTab)

    def retranslateUi(self, HomeTab):
        _translate = QtCore.QCoreApplication.translate
        HomeTab.setWindowTitle(_translate("HomeTab", "Form"))
        self.Header1.setText(_translate("HomeTab", "P.A.T."))
        self.Header2_1.setText(_translate("HomeTab", "Personal"))
        self.Header2_2.setText(_translate("HomeTab", "Admin"))
        self.Header2_3.setText(_translate("HomeTab", "Tool"))

from MyQtness.analogclock import PyAnalogClock
