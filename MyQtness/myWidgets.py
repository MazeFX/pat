# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation
# TODO - replace prints with logs for the lumberjack

"""
File: myWidgets.py
Creator: MazeFX
Date: 5-8-2016

Python Test docstring.
"""

import os

from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import QCoreApplication, Qt, pyqtProperty, pyqtSignal, QDate
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QTableView, QAbstractItemView, \
    QFrame, QComboBox, QLineEdit, QLabel, QItemDelegate, QRadioButton, QSpinBox

import logging
Lumberjack = logging.getLogger(__name__)

from colorama import Fore, Back, Style


class MyTableView(QTableView):

    _currentSelectedRow = None

    def __init__(self, *args):
        super(MyTableView, self).__init__(*args)

        # FIXME - Sort does not work on foreign column

        # TableView settings
        self.setShowGrid(True)
        self.setTabKeyNavigation(False)
        self.setProperty("showDropIndicator", False)
        self.setDragEnabled(False)
        self.setDragDropOverwriteMode(False)
        self.setAlternatingRowColors(True)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setTextElideMode(Qt.ElideMiddle)
        self.setSortingEnabled(True)

        # enable sorting
        self.setSortingEnabled(True)
        # set column width to fit contents
        self.resizeColumnsToContents()

        # hide vertical header
        vh = self.verticalHeader()
        vh.setVisible(False)
        vh.setHighlightSections(False)

        # set horizontal header properties
        hh = self.horizontalHeader()
        hh.setStretchLastSection(False)
        hh.setSectionsMovable(True)
        hh.setSortIndicatorShown(True)
        hh.setHighlightSections(False)

    def selectionChanged(self, QItemSelection, QItemSelection_1):
        Lumberjack.info('< MyTableView > - -> (selectionChanged)')
        super(MyTableView, self).selectionChanged(QItemSelection, QItemSelection_1)
        if not QItemSelection.isEmpty():
            self.setCurrentRow(QItemSelection.indexes()[0].row())

    def removeSelection(self):
        Lumberjack.info('< MyTableView > - -> (removeSelection)')
        self.clearSelection()
        self._currentSelectedRow = None

    def setCurrentRow(self, index):
        self._currentSelectedRow = index

    def getCurrentRow(self, *args):
        return self._currentSelectedRow

    currentSelectedRow = pyqtProperty(int, fget=getCurrentRow, fset=setCurrentRow)


class MyComboBox(QComboBox):

    # Emitted when selection of combobox changes
    _currentItem = None

    def __init__(self, *args):
        super(MyComboBox, self).__init__(*args)
        self.currentIndexChanged.connect(self.indexChanged)

    def getCurrentItem(self):

        return self._currentItem

    def indexChanged(self, index):
        self._currentItem = self.model().results[index]

    def setCurrentItem(self, item):

        model = self.model()
        for row in model.results:
            if hasattr(row, 'id'):
                if hasattr(item, 'id'):
                    if row.id == item.id:
                        self.setCurrentIndex(model.results.index(row))
                        self._currentItem = item

    currentItem = pyqtProperty(object, fget=getCurrentItem, fset=setCurrentItem)


class MyDragDropBox(QFrame):

    _currentFile = None

    def __init__(self, *args):
        super(MyDragDropBox, self).__init__(*args)
        Lumberjack.info('spawning a << MyDragDropBox >>')
        print(Fore.GREEN + '--=== DRAGDROPBOX ===--')
        print(Fore.GREEN + 'Here come the inits!')
        print(Fore.GREEN + 'args: ', args)
        print(Fore.GREEN + '==--- DRAGDROPBOX ---==')

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DropLabel = QLabel(self)
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.DropLabel.setFont(font)
        self.DropLabel.setAlignment(Qt.AlignCenter)
        self.DropLabel.setObjectName("DropLabel")
        self.verticalLayout.addWidget(self.DropLabel)
        self.edit = False

    def dragEnterEvent(self, event):
        Lumberjack.info('< MyDragDropBox > - -> (getRecurrenceValue)')
        print(Fore.GREEN + '-- DRAGDROPBOX -- Enter with drag')
        print(Fore.GREEN + '-- DRAGDROPBOX -- passed event: ', event)
        if event.mimeData().hasUrls:
            print(Fore.GREEN + '-- DRAGDROPBOX -- event accepted.')
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        Lumberjack.info('< MyDragDropBox > - -> (getRecurrenceValue)')
        print(Fore.GREEN + '-- DRAGDROPBOX -- Dropped something??')
        print(Fore.GREEN + '-- DRAGDROPBOX -- passed event: ', event)
        if not self.edit:
            event.accept()
            return
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
            print(Fore.GREEN + '-- DRAGDROPBOX -- event accepted.')
            l = []
            for url in event.mimeData().urls():
                l.append(str(url.toLocalFile()))
            print(Fore.GREEN + '-- DRAGDROPBOX -- files recieved: ', l)
            self.setCurrentFile(l)
        else:
            event.ignore()

    def mouseDoubleClickEvent(self, QMouseEvent):
        Lumberjack.info('< MyDragDropBox > - -> (mouseDoubleClickEvent)')
        filename = self.getCurrentFile()
        print(Fore.GREEN + 'Current file name for opening = ', filename)
        if filename:
            if os.path.exists(filename):
                print(Fore.GREEN + 'Current file exists and now opening')
                os.startfile(filename)
        for attr in self.__dict__:
            Lumberjack.debug('(mouseDoubleClickEvent) - widget attr = {}'.format(attr))

    def getCurrentFile(self):
        Lumberjack.info('< MyDragDropBox > - -> (getCurrentFile)')
        print(Fore.GREEN + '-- DRAGDROPBOX -- Getting the file: ')
        print(Fore.GREEN + '---------------------------------------')
        print(Fore.GREEN + 'Current File = ', self._currentFile)
        print(Fore.GREEN + 'With Type = ', type(self._currentFile))
        return self._currentFile

    def setCurrentFile(self, file):
        Lumberjack.info('< MyDragDropBox > - -> (setCurrentFile)')
        print(Fore.GREEN + '-- DRAGDROPBOX -- Setting the file: ')
        print(Fore.GREEN + '---------------------------------------')
        print(Fore.GREEN + 'file value = ', file)
        print(Fore.GREEN + 'With Type = ', type(file))
        self._currentFile = file
        self.check_widget_layout()

    currentFile = pyqtProperty(str, fget=getCurrentFile, fset=setCurrentFile)

    def check_widget_layout(self):
        Lumberjack.info('< MyDragDropBox > - -> (check_widget_layout)')
        print(Fore.GREEN + '-- DRAGDROPBOX -- setting layout for: ', self.DropLabel)
        if self._currentFile:
            self.DropLabel.setText('Open File')
        else:
            self.DropLabel.setText('Drop File')


class MyCurrencyBox(QFrame):

    _amount = None

    def __init__(self, *args):
        super(MyCurrencyBox, self).__init__(*args)
        Lumberjack.info('spawning a << MyCurrencyBox >>')
        self.currencyBoxlayout = QHBoxLayout(self)
        self.currencyBoxlayout.setObjectName("currencyBoxlayout")
        self.currencyLabel = QLabel('€')
        self.euroLineEdit = QLineEdit()
        self.euroLineEdit.setText('0')
        self.euroLineEdit.setAlignment(Qt.AlignRight)
        self.euroLineEdit.setObjectName("euroLineEdit")
        euroValidator = QIntValidator()
        self.euroLineEdit.setValidator(euroValidator)
        self.euroLineEdit.setMaxLength(6)
        self.commaLabel = QLabel(',')
        self.centsLineEdit = QLineEdit()
        self.centsLineEdit.setText('00')
        self.euroLineEdit.setAlignment(Qt.AlignRight)
        self.centsLineEdit.setObjectName("centsLineEdit")
        centsValidator = QIntValidator(0, 99)
        self.centsLineEdit.setValidator(centsValidator)
        self.centsLineEdit.setMaxLength(2)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.currencyBoxlayout.addItem(spacerItem1)
        self.currencyBoxlayout.addWidget(self.currencyLabel)
        self.currencyBoxlayout.addWidget(self.euroLineEdit)
        self.currencyBoxlayout.addWidget(self.commaLabel)
        self.currencyBoxlayout.addWidget(self.centsLineEdit)
        self.currencyBoxlayout.addItem(spacerItem2)

        self.centsLineEdit.textChanged.connect(self.on_text_input)
        self.euroLineEdit.textChanged.connect(self.on_text_input)

    def getAmount(self):
        Lumberjack.info('< MyCurrencyBox > - -> (getAmount)')
        if self._amount is None:
            return None
        euros = self.euroLineEdit.text()
        cents = self.centsLineEdit.text()
        full_amount = euros + cents
        self._amount = int(full_amount)
        return self._amount

    def setAmount(self, amount):
        Lumberjack.info('< MyCurrencyBox > - -> (setAmount)')
        if amount is None:
            self._amount = None
            euros = '0'
            cents = '00'
        else:
            euros = str(amount)[:-2]
            if euros == '':
                euros = '0'
            cents = str(amount)[-2:]
            if cents == '0':
                cents = '00'
        self.euroLineEdit.setText(euros)
        self.centsLineEdit.setText(cents)
        self._amount = amount

    amount = pyqtProperty(int, fget=getAmount, fset=setAmount)

    def on_text_input(self):
        Lumberjack.info('< MyCurrencyBox {}> - -> (on_text_input)')
        euros = self.euroLineEdit.text()
        cents = self.centsLineEdit.text()
        full_amount = euros + cents
        self._amount = int(full_amount)


class MyRecurrenceBox(QFrame):
    # TODO - Build a occurrence selector for Contract model based on spinbox
    # Used information type is DateTime.TimeDelta

    valueSet = pyqtSignal(bool)
    _recurrenceValue = None

    def __init__(self, *args):
        super(MyRecurrenceBox, self).__init__(*args)
        Lumberjack.info('spawning a << MyRecurrenceBox >>')
        _translate = QCoreApplication.translate

        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.spinBox = QSpinBox(self)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(1)
        self.verticalLayout.addWidget(self.spinBox)
        self.spinBox.valueChanged.connect(self.on_value_spin)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.dailyRadioButton = QRadioButton(self)
        self.dailyRadioButton.setObjectName("dailyRadioButton")
        self.horizontalLayout_2.addWidget(self.dailyRadioButton)
        self.dailyRadioButton.setText(_translate("Form", "Days"))
        self.dailyRadioButton.setChecked(True)
        self.selected_radio_button = self.dailyRadioButton
        self.dailyRadioButton.toggled.connect(self.on_radio_toggle)

        self.weeklyRadioButton = QRadioButton(self)
        self.weeklyRadioButton.setObjectName("weeklyRadioButton")
        self.horizontalLayout_2.addWidget(self.weeklyRadioButton)
        self.weeklyRadioButton.setText(_translate("Form", "Weeks"))
        self.weeklyRadioButton.toggled.connect(self.on_radio_toggle)

        self.monthlyRadioButton = QRadioButton(self)
        self.monthlyRadioButton.setObjectName("monthlyRadioButton")
        self.horizontalLayout_2.addWidget(self.monthlyRadioButton)
        self.monthlyRadioButton.setText(_translate("Form", "Months"))
        self.monthlyRadioButton.toggled.connect(self.on_radio_toggle)

        self.yearlyRadioButton = QRadioButton(self)
        self.yearlyRadioButton.setObjectName("yearlyRadioButton")
        self.horizontalLayout_2.addWidget(self.yearlyRadioButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.yearlyRadioButton.setText(_translate("Form", "Years"))
        self.yearlyRadioButton.toggled.connect(self.on_radio_toggle)

        self.radio_buttons = [self.dailyRadioButton,
                              self.weeklyRadioButton,
                              self.monthlyRadioButton,
                              self.yearlyRadioButton]

    def getRecurrenceValue(self):
        Lumberjack.info('< MyRecurrenceBox > - -> (getRecurrenceValue)')
        return self._recurrenceValue

    def setRecurrenceValue(self, rel_delta):
        Lumberjack.info('< MyRecurrenceBox > - -> (setRecurrenceValue)')
        self._recurrenceValue = rel_delta
        Lumberjack.debug('(setRecurrenceValue) - rel_delta = {}'.format(rel_delta))
        if rel_delta is None:
            self._recurrenceValue = None
        else:
            for kw in rel_delta:
                for radio_button in self.radio_buttons:
                    if kw == radio_button.text().lower():
                        Lumberjack.debug('(setRecurrenceValue) - checking radiobutton = {}'.format(radio_button.text()))
                        radio_button.setChecked(True)
                        self.spinBox.setValue(rel_delta[kw])

        if self._recurrenceValue is None:
            self.valueSet.emit(False)
        else:
            self.valueSet.emit(True)

    recurrenceValue = pyqtProperty(dict, fget=getRecurrenceValue, fset=setRecurrenceValue)

    def on_radio_toggle(self, *args):
        Lumberjack.info('< MyRecurrenceBox > - -> (on_radio_toggle)')
        activate = args[0]
        Lumberjack.debug('(on_toggle) - args = {}'.format(activate))
        if not activate:
            return

        for radio_button in self.radio_buttons:
            if radio_button.isChecked():
                self.selected_radio_button = radio_button
                Lumberjack.debug('(on_toggle) - selected radiobutton.text = {}'.format(radio_button.text()))
        rel_delta = self._calculate_value()
        self._recurrenceValue = rel_delta

    def on_value_spin(self, x):
        Lumberjack.info('< MyRecurrenceBox > - -> (on_value_spin)')
        rel_delta = self._calculate_value()
        self._recurrenceValue = rel_delta

    def _calculate_value(self):
        Lumberjack.info('< MyRecurrenceBox > - -> (_calculate_value)')
        x = self.spinBox.value()
        kw = self.selected_radio_button.text().lower()
        timespan = {kw: x}
        Lumberjack.debug('(_calculate_value) - calculated value = {} {}'.format(timespan, type(timespan)))
        return timespan


class MyItemDelegate(QItemDelegate):

    def __init__(self, *args):
        super(MyItemDelegate, self).__init__(*args)
        Lumberjack.info('spawning a << MyItemDelegate >>')

    def setEditorData(self, widget, modelIndex):
        Lumberjack.info('< MyItemDelegate > - -> (setEditorData)')
        if hasattr(widget, 'currentIndex'):
            widget.currentItem = modelIndex.data(role=Qt.EditRole)

        elif hasattr(widget, 'currentFile'):
            widget.currentFile = modelIndex.data(role=Qt.EditRole)

        elif hasattr(widget, 'isChecked'):
            widget.setChecked(modelIndex.data(role=Qt.EditRole))

        elif hasattr(widget, 'date'):
            date = str(modelIndex.data(role=Qt.EditRole))
            qtDate = QDate.fromString(date, 'yyyy-MM-dd')
            widget.setDate(qtDate)

        elif hasattr(widget, 'amount'):
            value = modelIndex.data(role=Qt.EditRole)
            Lumberjack.debug('(setEditorData) - amount = {}({})'.format(type(value), value))
            widget.amount = value

        elif hasattr(widget, 'text'):
            widget.setText(modelIndex.data())

        elif hasattr(widget, 'recurrenceValue'):
            widget.recurrenceValue = modelIndex.data(role=Qt.EditRole)

        else:
            Lumberjack.warning('(setEditorData) - NO MATCH FOUND!')
            Lumberjack.debug('(setEditorData) - mismatching widget = {}'.format(widget))
            for attr in widget.__dict__:
                Lumberjack.debug('(setEditorData) - widget attr = {}'.format(attr))

    def setModelData(self, widget, abstractItemModel, modelIndex):
        if hasattr(widget, 'currentIndex'):
            abstractItemModel.setData(modelIndex, widget.currentItem)
        elif hasattr(widget, 'currentFile'):
            abstractItemModel.setData(modelIndex, widget.currentFile)
        elif hasattr(widget, 'isChecked'):
            abstractItemModel.setData(modelIndex, widget.isChecked())
        elif hasattr(widget, 'date'):
            abstractItemModel.setData(modelIndex, widget.date())
        elif hasattr(widget, 'text'):
            abstractItemModel.setData(modelIndex, widget.text())
        elif hasattr(widget, 'amount'):
            abstractItemModel.setData(modelIndex, widget.amount)
        elif hasattr(widget, 'recurrenceValue'):
            abstractItemModel.setData(modelIndex, widget.recurrenceValue)
