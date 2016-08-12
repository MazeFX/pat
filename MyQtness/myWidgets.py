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
from PyQt5.QtWidgets import QTableView, QAbstractItemView, QComboBox


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
    indexChanged = pyqtSignal(int)

    def __init__(self, *args):
        super(MyComboBox, self).__init__(*args)

    def getItemIndex(self):
        print('Getting the item index', self.currentIndex())
        return self.currentIndex()

    def setItemIndex(self, index):
        print('Setting the item index', index)
        self.setCurrentIndex(index)

    itemIndex = pyqtProperty(int, fget=getItemIndex, fset=setItemIndex)

