# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: myWidgets.py
Creator: MazeFX
Date: 5-8-2016

Python Test docstring.
"""

import operator
import datetime

from PyQt5.QtCore import Qt, pyqtProperty, pyqtSignal, QDate
from PyQt5.QtWidgets import QTableView, QAbstractItemView, QWidget, QComboBox, QItemDelegate
from colorama import Fore, Back, Style


class MyTableView(QTableView):

    _currentSelectedRow = None

    def __init__(self, *args):
        super(MyTableView, self).__init__(*args)

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
        print(Fore.CYAN + 'Setting current Row for Tableview ', self.currentIndex())

    def setCurrentRow(self, index):
        print(Fore.CYAN + 'Setting current Row for Tableview ', index)
        self._currentSelectedRow = index

    def selectionChanged(self, QItemSelection, QItemSelection_1):
        super(MyTableView, self).selectionChanged(QItemSelection, QItemSelection_1)
        if not QItemSelection.isEmpty():
            print(Fore.CYAN + 'Syncing the form with sent args: ', QItemSelection)
            print(Fore.CYAN + 'index with value: ', QItemSelection.indexes())
            print(Fore.CYAN + 'index with row: ', QItemSelection.indexes()[0].row())
            self.setCurrentRow(QItemSelection.indexes()[0].row())

    def getCurrentRow(self, *args):
        print(Fore.CYAN + 'Setting current Row for Tableview ', args)
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


class MyDragDropBox(QWidget):

    # Emitted when selection of combobox changes
    _currentFile = None

    def __init__(self, *args):
        super(MyDragDropBox, self).__init__(*args)
        # self.currentIndexChanged.connect(self.indexChanged)

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

    def getCurrentFile(self):
        print(Fore.GREEN + '-- DRAGDROPBOX -- Getting the file: ')
        print(Fore.GREEN + '---------------------------------------')
        return self._currentFile

    def setCurrentFile(self, file):
        print(Fore.GREEN + '-- DRAGDROPBOX -- Setting the file: ', file[0])
        self._currentFile = file[0]

    currentFile = pyqtProperty(object, fget=getCurrentFile, fset=setCurrentFile)


class MyItemDelegate(QItemDelegate):

    def __init__(self, *args):
        super(MyItemDelegate, self).__init__(*args)

    def setEditorData(self, widget, modelIndex):
        print(Fore.RED + 'Itemdelegate - setEditorData; modelindex: ', modelIndex)
        if hasattr(widget, 'currentIndex'):
            widget.currentItem = modelIndex.data(role=Qt.EditRole)

        elif hasattr(widget, 'currentFile'):
            widget.currentFile = [modelIndex.data(role=Qt.EditRole)]

        elif hasattr(widget, 'date'):
            print(Fore.RED + '--Trying to set current date for: ', widget)
            print(Fore.RED + '--at index: ', modelIndex.row(), ', ', modelIndex.column())
            print(Fore.RED + '--with date??: ', modelIndex.data())

            print(Fore.RED + '--setting widget.date: ', type(modelIndex.data(role=Qt.EditRole)))
            date = str(modelIndex.data(role=Qt.EditRole))
            qtDate = QDate.fromString(date, 'yyyy-MM-dd')
            widget.setDate(qtDate)

        elif hasattr(widget, 'text'):
            text = modelIndex.data()
            widget.setText(text)

    def setModelData(self, widget, abstractItemModel, modelIndex):
        print(Back.GREEN + Fore.RED + 'Itemdelegate - setModelData; modelindex: ', modelIndex)
        if hasattr(widget, 'currentIndex'):
            abstractItemModel.setData(modelIndex, widget.currentItem)
        elif hasattr(widget, 'currentFile'):
            abstractItemModel.setData(modelIndex, widget.currentFile)
        elif hasattr(widget, 'date'):
            abstractItemModel.setData(modelIndex, widget.date())
        elif hasattr(widget, 'text'):
            abstractItemModel.setData(modelIndex, widget.text())
