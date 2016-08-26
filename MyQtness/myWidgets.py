# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: myWidgets.py
Creator: MazeFX
Date: 5-8-2016

Python Test docstring.
"""

import os
import operator
import datetime

from PyQt5.QtGui import QFont, QPainter
from PyQt5.QtCore import Qt, pyqtProperty, pyqtSignal, QDate
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QTableView, QAbstractItemView, \
    QFrame, QComboBox, QLabel, QItemDelegate, QStyleOption, QStyle
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

    def setCurrentRow(self, index):
        self._currentSelectedRow = index

    def selectionChanged(self, QItemSelection, QItemSelection_1):
        super(MyTableView, self).selectionChanged(QItemSelection, QItemSelection_1)
        if not QItemSelection.isEmpty():
            self.setCurrentRow(QItemSelection.indexes()[0].row())

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
                        self.setCurrentIndex(row.id - 1)
                        self._currentItem = item

    currentItem = pyqtProperty(object, fget=getCurrentItem, fset=setCurrentItem)


class MyDragDropBox(QFrame):

    # Emitted when selection of combobox changes
    _currentFile = None

    def __init__(self, *args, **kwargs):
        super(MyDragDropBox, self).__init__(*args)
        print(Fore.GREEN + '--=== DRAGDROPBOX ===--')
        print(Fore.GREEN + 'Here come the inits!')
        print(Fore.GREEN + 'args: ', args)
        print(Fore.GREEN + 'kwargs: ', kwargs)
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
        print(Fore.GREEN + '-- DRAGDROPBOX -- setting layout for: ', self.DropLabel)
        self.edit = False



    def dragEnterEvent(self, event):
        print(Fore.GREEN + '-- DRAGDROPBOX -- Enter with drag')
        print(Fore.GREEN + '-- DRAGDROPBOX -- passed event: ', event)
        if event.mimeData().hasUrls:
            print(Fore.GREEN + '-- DRAGDROPBOX -- event accepted.')
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
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
        print(Fore.GREEN + '-- DRAGDROPBOX -- Registered a double click')
        filename = self.getCurrentFile()
        print(Fore.GREEN + 'Current file name for opening = ', filename)
        if filename:
            if os.path.exists(filename):
                print(Fore.GREEN + 'Current file exists and now opening')
                os.startfile(filename)

    def getCurrentFile(self):
        print(Fore.GREEN + '-- DRAGDROPBOX -- Getting the file: ')
        print(Fore.GREEN + '---------------------------------------')
        print(Fore.GREEN + 'Current File = ', self._currentFile)
        print(Fore.GREEN + 'With Type = ', type(self._currentFile))
        return self._currentFile

    def setCurrentFile(self, file):
        print(Fore.GREEN + '-- DRAGDROPBOX -- Setting the file: ')
        print(Fore.GREEN + '---------------------------------------')
        print(Fore.GREEN + 'file value = ', file)
        print(Fore.GREEN + 'With Type = ', type(file))
        self._currentFile = file
        self.check_widget_layout()

    currentFile = pyqtProperty(str, fget=getCurrentFile, fset=setCurrentFile)

    def check_widget_layout(self):
        print(Fore.GREEN + '-- DRAGDROPBOX -- setting layout for: ', self.DropLabel)
        if self._currentFile:
            self.DropLabel.setText('Open File')
        else:
            self.DropLabel.setText('Drop File')


class MyOccurrenceBox(QHBoxLayout):
    # TODO - Build a occurrence selector for Contract model based on spinbox
    pass


class MyItemDelegate(QItemDelegate):

    def __init__(self, *args):
        super(MyItemDelegate, self).__init__(*args)

    def setEditorData(self, widget, modelIndex):
        if hasattr(widget, 'currentIndex'):
            widget.currentItem = modelIndex.data(role=Qt.EditRole)

        elif hasattr(widget, 'currentFile'):
            widget.currentFile = modelIndex.data(role=Qt.EditRole)

        elif hasattr(widget, 'date'):
            date = str(modelIndex.data(role=Qt.EditRole))
            qtDate = QDate.fromString(date, 'yyyy-MM-dd')
            widget.setDate(qtDate)

        elif hasattr(widget, 'text'):
            text = modelIndex.data()
            widget.setText(text)

    def setModelData(self, widget, abstractItemModel, modelIndex):
        if hasattr(widget, 'currentIndex'):
            abstractItemModel.setData(modelIndex, widget.currentItem)
        elif hasattr(widget, 'currentFile'):
            abstractItemModel.setData(modelIndex, widget.currentFile)
        elif hasattr(widget, 'date'):
            abstractItemModel.setData(modelIndex, widget.date())
        elif hasattr(widget, 'text'):
            abstractItemModel.setData(modelIndex, widget.text())
