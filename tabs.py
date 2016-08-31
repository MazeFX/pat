# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: tabs.py
Creator: MazeFX
Date: 5-8-2016

Python Test docstring.
"""


from PyQt5 import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTableView, QLabel

from forms import BankAccountForm, ContractForm, EmailAddressForm, LetterForm, \
     RelationForm, TransactionForm, UserForm
from db.models import AlchemicalTableModel, BankAccount, Contract, EmailAddress, Letter, \
     Relation, Transaction, User 
from MyQtness.myWidgets import MyTableView
from MyQtness.ui_home_tab import Ui_HomeTab
from colorama import Fore, Back, Style

import logging
Lumberjack = logging.getLogger(__name__)


class HomeTab(QWidget, Ui_HomeTab):

    dbhelper = None

    def __init__(self, dbhelper, *args):
        super(HomeTab, self).__init__(*args)
        Lumberjack.info('spawning a << HomeTab >>')
        self.dbhelper = dbhelper

        self.setupUi(self)

        myPixmap = QPixmap(':/app_icons/rc/PAT_Logo.png')
        myScaledPixmap = myPixmap.scaledToHeight(200)
        self.LogoContainer.setPixmap(myScaledPixmap)

    def showEvent(self, *args):
        Lumberjack.info('< HomeTab > - -> (showEvent)')
        self.refresh_stats()

    def refresh_stats(self):
        statistics = self.dbhelper.get_table_statistics()
        for stat in statistics:
            value = statistics[stat]
            lcd_string = stat + 'Number'
            if hasattr(self, lcd_string):
                lcdWidget = getattr(self, lcd_string)
                lcdWidget.display(value)


class BankAccountListTab(QWidget):

    dbhelper = None

    def __init__(self, dbhelper, *args):
        super(BankAccountListTab, self).__init__(*args)
        Lumberjack.info('spawning a << BankAccountListTab >>')
        self.dbhelper = dbhelper

        self.horizontalLayout = QHBoxLayout(self)

        model = AlchemicalTableModel(
            self.dbhelper.get_app_db_session(),
            BankAccount,
            [('Bank name', BankAccount.bank_name, 'bank_name', {}),
             ('User', BankAccount.user, 'user.name', {}),
             ('Account Nr.', BankAccount.account, 'account', {}),
             ('Balance', BankAccount.balance, 'balance', {'type': 'currency', }),
             ('Date created', BankAccount.date_created, 'date_created', {})])
        # TODO - Create visual effect for negative balance or amount eg: green for positive, red for negative.

        self.tableView = MyTableView()
        self.tableView.setModel(model)

        self.form = BankAccountForm(model, self.dbhelper)
        self.form.tableBuddy = self.tableView
        selectionModel = self.tableView.selectionModel()
        selectionModel.selectionChanged.connect(self.form.set_mapper_index_from_selection)

        self.horizontalLayout.addWidget(self.form)
        self.horizontalLayout.addWidget(self.tableView)

        self.setLayout(self.horizontalLayout)


class ContractListTab(QWidget):

    dbhelper = None

    def __init__(self, dbhelper, *args):
        super(ContractListTab, self).__init__(*args)
        Lumberjack.info('spawning a << ContractListTab >>')
        self.dbhelper = dbhelper

        self.horizontalLayout = QHBoxLayout(self)

        model = AlchemicalTableModel(
            self.dbhelper.get_app_db_session(),
            Contract,
            [('Relation', Contract.relation, 'relation.name', {}),
             ('User', Contract.user, 'user.name', {}),
             ('Bank account', Contract.account, 'account.account', {}),
             ('Letter', Contract.letter, 'letter.reference', {}),
             ('Email', Contract.email, 'email.address', {}),
             ('Amount', Contract.amount, 'amount', {}),
             ('Recurrence', Contract.recurrence, 'recurrence', {}),
             ('Start date', Contract.start_date, 'start_date', {}),
             ('End date', Contract.end_date, 'end_date', {}),
             ('Date created', Contract.date_created, 'date_created', {})])

        self.tableView = MyTableView()
        self.tableView.setModel(model)

        self.form = ContractForm(model, self.dbhelper)
        selectionModel = self.tableView.selectionModel()
        selectionModel.selectionChanged.connect(self.form.set_mapper_index_from_selection)

        self.horizontalLayout.addWidget(self.form)
        self.horizontalLayout.addWidget(self.tableView)

        self.setLayout(self.horizontalLayout)


class EmailAddressListTab(QWidget):

    dbhelper = None

    def __init__(self, dbhelper, *args):
        super(EmailAddressListTab, self).__init__(*args)
        Lumberjack.info('spawning a << EmailAddressListTab >>')
        self.dbhelper = dbhelper

        self.horizontalLayout = QHBoxLayout(self)

        model = AlchemicalTableModel(
            self.dbhelper.get_app_db_session(),
            EmailAddress,
            [('User', EmailAddress.user, 'user.fullname', {}),
             ('Address', EmailAddress.address, 'address', {}),
             ('Date created', EmailAddress.date_created, 'date_created', {})])

        self.tableView = MyTableView()
        self.tableView.setModel(model)

        self.form = EmailAddressForm(model, self.dbhelper)
        selectionModel = self.tableView.selectionModel()
        selectionModel.selectionChanged.connect(self.form.set_mapper_index_from_selection)

        self.horizontalLayout.addWidget(self.form)
        self.horizontalLayout.addWidget(self.tableView)

        self.setLayout(self.horizontalLayout)


class LetterListTab(QWidget):

    dbhelper = None

    def __init__(self, dbhelper, *args):
        super(LetterListTab, self).__init__(*args)
        Lumberjack.info('spawning a << LetterListTab >>')
        self.dbhelper = dbhelper

        self.horizontalLayout = QHBoxLayout(self)

        model = AlchemicalTableModel(
            self.dbhelper.get_app_db_session(),
            Letter,
            [('Date', Letter.date, 'date', {}),
             ('Subject', Letter.subject, 'subject', {}),
             ('Sender', Letter.relation, 'relation.name', {}),
             ('Reference', Letter.reference, 'reference', {}),
             ('User', Letter.user, 'user.fullname', {}),
             ('Letter scan', Letter.scan_file, 'scan_file', {}),
             ('Letter type', Letter.letter_type, 'letter_type.letter', {}),
             ('Date created', Letter.date_created, 'date_created', {})])

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

    def __init__(self, dbhelper, *args):
        super(RelationListTab, self).__init__(*args)
        Lumberjack.info('spawning a << RelationListTab >>')
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
             ('Date created', Relation.date_created, 'date_created', {})])

        self.tableView = MyTableView()
        self.tableView.setModel(model)

        self.form = RelationForm(model, self.dbhelper)
        selectionModel = self.tableView.selectionModel()
        selectionModel.selectionChanged.connect(self.form.set_mapper_index_from_selection)

        self.horizontalLayout.addWidget(self.form)
        self.horizontalLayout.addWidget(self.tableView)

        self.setLayout(self.horizontalLayout)


class TransactionListTab(QWidget):

    dbhelper = None

    def __init__(self, dbhelper, *args):
        super(TransactionListTab, self).__init__(*args)
        Lumberjack.info('spawning a << TransactionListTab >>')
        self.dbhelper = dbhelper

        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")

        model = AlchemicalTableModel(
            self.dbhelper.get_app_db_session(),
            Transaction,
            [('Contract', Transaction.contract, 'contract.reference', {}),
             ('Letter', Transaction.letter, 'letter.reference', {}),
             ('Bank account', Transaction.account, 'account.account', {}),
             ('Amount', Transaction.amount, 'amount', {}),
             ('Transaction date', Transaction.transaction_date, 'transaction_date', {}),
             ('Payment date', Transaction.payment_date, 'payment_date', {}),
             ('Payed?', Transaction.payment_state, 'payment_state', {}),
             ('Debit/Credit', Transaction.debit, 'debit', {}),
             ('Date created', Transaction.date_created, 'date_created', {})])

        self.tableView = MyTableView()
        self.tableView.setModel(model)

        self.form = TransactionForm(model, self.dbhelper)
        selectionModel = self.tableView.selectionModel()
        selectionModel.selectionChanged.connect(self.form.set_mapper_index_from_selection)

        self.horizontalLayout.addWidget(self.form)
        self.horizontalLayout.addWidget(self.tableView)

        self.setLayout(self.horizontalLayout)


class UserListTab(QWidget):

    dbhelper = None

    def __init__(self, dbhelper, *args):
        super(UserListTab, self).__init__(*args)
        self.dbhelper = dbhelper

        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")

        model = AlchemicalTableModel(
            self.dbhelper.get_app_db_session(),
            User,
            [('Name', User.name, 'name', {}),
             ('Full Name', User.fullname, 'fullname', {}),
             ('Password', User.password, 'password', {}),
             ('Date created', User.date_created, 'date_created', {})])

        self.tableView = MyTableView()
        self.tableView.setModel(model)

        self.form = UserForm(model, self.dbhelper)
        selectionModel = self.tableView.selectionModel()
        selectionModel.selectionChanged.connect(self.form.set_mapper_index_from_selection)

        self.horizontalLayout.addWidget(self.form)
        self.horizontalLayout.addWidget(self.tableView)

        self.setLayout(self.horizontalLayout)






