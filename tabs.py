# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: tabs.py
Creator: MazeFX
Date: 5-8-2016

Python Test docstring.
"""

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTableView

from forms import LetterForm, UserForm, RelationForm
from db.models import AlchemicalTableModel, Letter, User, Relation
from MyQtness.myWidgets import MyTableView
from MyQtness.ui_home_tab import Ui_HomeTab
from colorama import Fore, Back, Style


class HomeTab(QWidget, Ui_HomeTab):

    def __init__(self, *args):
        super(HomeTab, self).__init__(*args)

        self.setupUi(self)
        # TODO - Create some statitics widgets for showing data


class LetterListTab(QWidget):

    dbhelper = None

    def __init__(self, dbhelper, **kwargs):
        super(LetterListTab, self).__init__(**kwargs)
        self.dbhelper = dbhelper

        self.horizontalLayout = QHBoxLayout(self)

        model = AlchemicalTableModel(
            self.dbhelper.get_app_db_session(),
            Letter,
            [('Date', Letter.date, 'date', {}),
             ('Subject', Letter.subject, 'subject', {}),
             ('Sender', Letter.sender, 'sender.name', {}),
             ('Reference', Letter.reference, 'reference', {}),
             ('User', Letter.user, 'user.fullname', {}),
             ('Letter scan', Letter.scan_file, 'scan_file', {}),
             ('Letter type', Letter.letter_type, 'letter_type.letter', {}),
             ('Date created', Letter.date_created, 'date_created', {})])

        print('Letter Tab model role names: ', model.roleNames())

        self.tableView = MyTableView()
        self.tableView.setModel(model)

        self.form = LetterForm(model, self.dbhelper)
        selectionModel = self.tableView.selectionModel()
        selectionModel.selectionChanged.connect(self.form.set_mapper_index_from_selection)

        self.horizontalLayout.addWidget(self.form)
        self.horizontalLayout.addWidget(self.tableView)

        self.setLayout(self.horizontalLayout)


class RelationListTab(QWidget):

    dbhelper = None

    def __init__(self, dbhelper, **kwargs):
        super(RelationListTab, self).__init__(**kwargs)
        self.dbhelper = dbhelper

        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")

        model = AlchemicalTableModel(
            self.dbhelper.get_app_db_session(),
            Relation,
            [('Name', Relation.name, 'name', {}),
             ('Full Name', Relation.fullname, 'fullname', {}),
             ('Reference', Relation.reference, 'reference', {}),
             ('Bank account', Relation.bank_account, 'bank_account', {}),
             ('Relation type', Relation.relation_type, 'relation_type.relation', {}),
             ('Start date', Relation.start_date, 'start_date', {}),
             ('End date', Relation.end_date, 'end_date', {}),
             ('Date created', Relation.date_created, 'date_created', {})])

        print('Letter Tab model role names: ', model.roleNames())

        self.tableView = MyTableView()
        self.tableView.setModel(model)

        self.form = RelationForm(model, self.dbhelper)
        selectionModel = self.tableView.selectionModel()
        selectionModel.selectionChanged.connect(self.form.set_mapper_index_from_selection)

        self.horizontalLayout.addWidget(self.form)
        self.horizontalLayout.addWidget(self.tableView)

        self.setLayout(self.horizontalLayout)


class UserListTab(QWidget):

    dbhelper = None

    def __init__(self, dbhelper, **kwargs):
        super(UserListTab, self).__init__(**kwargs)
        self.dbhelper = dbhelper

        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")

        model = AlchemicalTableModel(
            self.dbhelper.get_app_db_session(),
            User,
            [('Name', User.name, 'name', {}),
             ('Full Name', User.fullname, 'fullname', {}),
             ('Password', User.password, 'password', {})])

        print('Letter Tab model role names: ', model.roleNames())

        self.tableView = MyTableView()
        self.tableView.setModel(model)

        self.form = UserForm(model, self.dbhelper)
        selectionModel = self.tableView.selectionModel()
        selectionModel.selectionChanged.connect(self.form.set_mapper_index_from_selection)

        self.horizontalLayout.addWidget(self.form)
        self.horizontalLayout.addWidget(self.tableView)

        self.setLayout(self.horizontalLayout)






