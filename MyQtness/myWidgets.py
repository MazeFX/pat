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

from PyQt5.QtCore import Qt, QAbstractTableModel, QVariant
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableView


class myTableView(QWidget):

    def __init__(self, *args):
        super(myTableView, self).__init__(args[0])

        # create table
        tablemaker = args[1]
        print('1st tHis is the tablemaker.table_data: ')
        self.get_table_data(tablemaker)
        table = self.createTable()

        # layout
        layout = QVBoxLayout()
        layout.addWidget(table)
        self.setLayout(layout)

    def get_table_data(self, tablemaker):
        self.tabledata = tablemaker.table_data
        print('2de tHis is the tablemaker.table_data: ', tablemaker.table_data)
        self.headerdata = tablemaker.header_data

    def createTable(self):
        # create the view
        tv = QTableView()
        print('QTableView created.')

        # set the table model
        tm = MyTableModel(self.tabledata, self.headerdata, self)
        tv.setModel(tm)
        print('QTableView model set.')
        # set the minimum size
        tv.setMinimumSize(400, 300)

        # hide grid
        tv.setShowGrid(True)

        # set the font

        # hide vertical header
        vh = tv.verticalHeader()
        vh.setVisible(False)

        # set horizontal header properties
        hh = tv.horizontalHeader()
        hh.setStretchLastSection(True)
        hh.setSectionsMovable(True)
        hh.setSortIndicatorShown(True)

        # set column width to fit contents
        tv.resizeColumnsToContents()

        # set row height
        nrows = len(self.tabledata)
        for row in range(nrows):
            tv.setRowHeight(row, 18)

        # enable sorting
        tv.setSortingEnabled(True)


        return tv


class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None, *args):
        """ datain: a list of lists
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        self.layoutAboutToBeChanged.emit()
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.layoutChanged.emit()
