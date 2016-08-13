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

from PyQt5.QtCore import Qt, pyqtProperty, pyqtSignal
from PyQt5.QtWidgets import QTableView, QAbstractItemView, QComboBox, QItemDelegate
from colorama import Fore, Back, Style


class MyTableView(QTableView):

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


class MyComboBox(QComboBox):

    # Emitted when selection of combobox changes
    _currentItem = None

    def __init__(self, *args):
        super(MyComboBox, self).__init__(*args)
        self.currentIndexChanged.connect(self.indexChanged)

    def getCurrentItem(self):
        print(Fore.GREEN + '-- COMBOBOX -- Getting the item index: ')
        print(Fore.GREEN + '---------------------------------------')
        print(Fore.GREEN + '-- COMBOBOX - Model -- get model value row: ')
        print(Fore.GREEN + '-- COMBOBOX - get row matches with item: ')
        return self._currentItem

    def indexChanged(self, index):
        self._currentItem = self.model().results[index]

    def setCurrentItem(self, item):
        print(Fore.GREEN + '-- COMBOBOX -- Setting the item: ', item, str(item))
        model = self.model()
        for row in model.results:
            print(Fore.GREEN + '-- COMBOBOX - Model -- model value row: ', row, str(row))
            if hasattr(row, 'id'):
                if hasattr(item, 'id'):
                    if row.id == item.id:
                        print(Fore.GREEN + '-- COMBOBOX - row matches with item: ', row, str(row))
                        self.setCurrentIndex(row.id - 1)
                        self._currentItem = item

    currentItem = pyqtProperty(object, fget=getCurrentItem, fset=setCurrentItem)


class MyItemDelegate(QItemDelegate):

    def __init__(self, *args):
        super(MyItemDelegate, self).__init__(*args)

    def setEditorData(self, widget, modelIndex):
        print(Fore.RED + 'Itemdelegate - setEditorData; modelindex: ', modelIndex)
        if hasattr(widget, 'currentIndex'):
            print(Fore.RED + 'Trying to set current index for: ', widget)
            print(Fore.RED + 'at index: ', modelIndex.row(), ', ', modelIndex.column())
            print(Fore.RED + 'with value: ', modelIndex.data())
            if modelIndex.data() not in ('-2', ''):
                widget.currentItem = modelIndex.data(role=Qt.EditRole)

    def setModelData(self, widget, abstractItemModel, modelIndex):
        print(Back.GREEN + 'Itemdelegate - setModelData; modelindex: ', modelIndex)
        if hasattr(widget, 'currentIndex'):
            abstractItemModel.setData(modelIndex, widget.currentItem)
