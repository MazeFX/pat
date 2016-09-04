# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: forms_refactor.py
Creator: MazeFX
Date: 22-8-2016

Python Test docstring.
"""

import sys

from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QCoreApplication, Qt, QDate, QModelIndex, QRegExp, QSize, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QDataWidgetMapper, QPushButton, QFormLayout

from db.models import AlchemicalTableModel, TypeModel, BankAccount, Contract, EmailAddress, \
    Letter, Relation, Type, User
from db.helper import DbHelper, DbFileHandler

from MyQtness.ui_basic_form import Ui_BasicForm
from MyQtness.ui_bank_account_form import Ui_BankAccountFormInsert
from MyQtness.ui_contract_form import Ui_ContractFormInsert
from MyQtness.ui_email_address_form import Ui_EmailAddressFormInsert
from MyQtness.ui_letter_form import Ui_LetterFormInsert
from MyQtness.ui_relation_form import Ui_RelationFormInsert
from MyQtness.ui_user_form import Ui_UserFormInsert
from MyQtness.ui_transaction_form import Ui_TransactionFormInsert
from MyQtness.myWidgets import MyItemDelegate
from dialogs import SaveDialog, DeleteDialog

import qtawesome as qta

import logging
Lumberjack = logging.getLogger(__name__)

from colorama import Fore, Back, Style


class BasicForm(QWidget, Ui_BasicForm):
    '''
    Basic form class for creating tab forms.
    Class is not to be used. Use form class inhereting
    from this class.
    '''

    tableBuddy = None
    dbhelper = None
    model = None
    field_list = []

    def __init__(self, model, db_helper, *args):
        super(BasicForm, self).__init__(*args)
        Lumberjack.info('spawning a << BasicForm >>')

        self.setupUi(self)
        self.edit_mode = None
        self.dbhelper = db_helper
        self.model = model
        print(Fore.GREEN + 'Model from init: ', self.model)
        print(Fore.GREEN + 'dbhelper from init: ', self.dbhelper)


        self.pushButtonAdd.setFocusPolicy(Qt.NoFocus)
        self.pushButtonAdd.clicked.connect(self.on_add)

        self.pushButtonEdit.setFocusPolicy(Qt.NoFocus)
        self.pushButtonEdit.clicked.connect(self.on_edit)

        self.pushButtonDelete.setFocusPolicy(Qt.NoFocus)
        self.pushButtonDelete.clicked.connect(self.on_delete)

        self.pushButtonSave.setFocusPolicy(Qt.NoFocus)
        self.pushButtonSave.clicked.connect(self.on_save)

        self.pushButtonCancel.setFocusPolicy(Qt.NoFocus)
        self.pushButtonCancel.clicked.connect(self.on_cancel)

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        print(Fore.CYAN + 'mapper created: ', self.mapper)
        delegate = MyItemDelegate(self)
        self.mapper.setItemDelegate(delegate)

        self.mapper.setModel(self.model)

    def set_mapper(self):
        pass

    def set_mapper_index_from_selection(self, QItemSelection, QItemSelection_1):
        Lumberjack.info('< BasicForm > - -> (set_mapper_index_from_selection)')
        if QItemSelection.isEmpty():
            return
        if self.edit_mode:
            self.toggle_edit_mode(False, None, None)

        selected_index = QItemSelection.indexes()
        row_index = selected_index[0].row()
        self.mapper.setCurrentIndex(row_index)

    def set_controls(self):
        pass

    def toggle_edit_mode(self, flag, mode, row):
        Lumberjack.info('< BasicForm > - -> (toggle_edit_mode)')
        print(Fore.CYAN + 'Setting edit mode for letter form: ', flag, mode)

        if flag and self.edit_mode is None:
            self.openItem = self.model.results[row]

        elif not flag and self.edit_mode:
            item_changed_saved = self.check_item_change()
            print(Fore.CYAN + 'Item Change saved: ', item_changed_saved)
            if item_changed_saved:
                self.openItem = None
            elif item_changed_saved is None:
                return
            else:
                if self.edit_mode == 'add':
                    self.model.rollbackRow(self.newRow)
                    self.newRow = None

        Lumberjack.debug('(toggle_edit_mode) -  set edit mode = {}'.format(mode))
        self.edit_mode = mode
        for field in self.field_list:
            if hasattr(field, 'edit'):
                field.edit = flag
            else:
                field.setEnabled(flag)

        if self.edit_mode is None or self.edit_mode == 'add':
            self.pushButtonCancel.setText('Cancel')
        if self.edit_mode == 'edit':
            self.pushButtonCancel.setText('Reset')

    def on_add(self):
        Lumberjack.info('< BasicForm > - -> (on_add)')
        # TODO - when adding new item remove current list selection
        if self.tableBuddy:
            self.tableBuddy.removeSelection()

        row = self.model.rowCount(None)
        self.newRow = row
        self.model.insertRow(row)
        print(Fore.CYAN + 'Row count after add: ', self.model.rowCount(None))
        self.mapper.setCurrentIndex(row)
        print(Fore.CYAN + 'New row at index: ', row)
        print(Fore.CYAN + 'mapper index: ', self.mapper.currentIndex())
        self.toggle_edit_mode(True, 'add', row)

    def on_edit(self):
        print(Fore.CYAN + 'Edit signal sent and recieved.')
        print(Fore.CYAN + 'mapper index: ', self.mapper.currentIndex())
        if self.edit_mode in ('add', 'edit'):
            self.toggle_edit_mode(False, None, None)
        elif self.mapper.currentIndex() >= 0:
            self.toggle_edit_mode(True, 'edit', self.mapper.currentIndex())

    def on_delete(self):
        Lumberjack.info('< BasicForm > - -> (on_delete)')
        delete_dialog = DeleteDialog()
        result = delete_dialog.exec_()
        if result == DeleteDialog.Accepted:
            Lumberjack.debug('(on_delete) - Deleting current selected row : {}'. format(self.mapper.currentIndex()))
            self.model.removeRow(self.mapper.currentIndex())
            if self.tableBuddy:
                self.tableBuddy.removeSelection()
            self.mapper.setCurrentIndex(0)

    def on_save(self):
        print(Fore.CYAN + 'Save signal sent and recieved.')
        if hasattr(self, 'save_check'):
            print(Fore.CYAN + 'Checking for onsave checks.')
            self.save_check()
        if self.edit_mode == 'edit':
            self.mapper.submit()
        elif self.edit_mode == 'add':
            self.model.storeRow(self.newRow)
            # TODO - Check sql insert unnecessary
            self.mapper.submit()
            self.NewRow = None
            self.edit_mode = None

        self.toggle_edit_mode(False, None, None)

    def check_item_change(self):
        # TODO - create check changes function.
        print(Fore.CYAN + '----- Starting Check of item change -----')
        changed = False
        old_item = self.openItem
        headers = [self.model.fields[x][2] for x in range(len(self.model.fields))]
        print(Fore.CYAN + '-Headers are: ', headers)
        for x in range(len(headers)):
            if '.' in headers[x]:
                foreign_column = headers[x].split('.')
                old_value = getattr(old_item, foreign_column[0])

            else:
                old_value = getattr(old_item, headers[x])
            print(Fore.CYAN + '-Old item value for: ', headers[x], 'with value: ', old_value)
            widget = self.mapper.mappedWidgetAt(x)
            if widget:
                if hasattr(widget, 'currentIndex'):
                    new_value = widget.currentItem
                    print(Fore.CYAN + '-New Widget value for: ', widget, 'with value: ', new_value)
                elif hasattr(widget, 'currentFile'):
                    new_value = widget.currentFile
                    print(Fore.CYAN + '-New Widget value for: ', widget, 'with value: ', new_value)
                elif hasattr(widget, 'date'):
                    new_value = widget.date()
                    print(Fore.CYAN + '-New Widget value for: ', widget, 'with value: ', new_value)
                elif hasattr(widget, 'text'):
                    new_value = widget.text()
                    print(Fore.CYAN + '-New Widget value for: ', widget, 'with value: ', new_value)
                elif hasattr(widget, 'amount'):
                    new_value = widget.amount
                    print(Fore.CYAN + '-New Widget value for: ', widget, 'with value: ', new_value)
                elif hasattr(widget, 'recurrenceValue'):
                    new_value = widget.recurrenceValue
                    print(Fore.CYAN + '-New Widget value for: ', widget, 'with value: ', new_value)

                if old_value == new_value:
                    print(Fore.CYAN + '++++ Matching value for: ', widget, 'with values: ', old_value, new_value)
                    changed = False
                else:
                    print(Fore.CYAN + '---- Not Matching value for: ', widget, 'with values: ', old_value, new_value)
                    changed = True
                    break

        print(Fore.CYAN + '++-----++ Did item change??: ', changed)

        if changed:
            save_dialog = SaveDialog()
            result = save_dialog.exec_()
            if result == SaveDialog.Success:
                self.mapper.submit()
                return True

            elif result == SaveDialog.Failed:
                print(Fore.YELLOW + '---- SaveDialog returned Failed: not Saving the item changes')
                return False
            elif result == SaveDialog.Rejected:
                print(Fore.YELLOW + '---- SaveDialog returned Rejected: dont do anything')
                return None
        else:
            return True

    def on_cancel(self):
        Lumberjack.info('< BasicForm > - -> (on_cancel)')
        Lumberjack.debug('(on_cancel) - edit mode = {}'.format(self.edit_mode))
        if self.edit_mode == 'add':
            # TODO - write cancel action: closing form and deleting projected row
            print(Fore.CYAN + 'Canceling the add action.')
            self.toggle_edit_mode(False, None, None)
            self.mapper.setCurrentIndex(0)
        if self.edit_mode == 'edit':
            self.mapper.revert()
        

class BankAccountForm(BasicForm, Ui_BankAccountFormInsert):

    def __init__(self, *args):
        super(BankAccountForm, self).__init__(*args)
        Ui_BankAccountFormInsert.setupUi(self, self.FormContainer)
        Ui_BankAccountFormInsert.retranslateUi(self, self.FormContainer)
        Lumberjack.info('evolving to a << BankAccountForm >>')

        for x in range(self.formLayout.rowCount()):
            widget = self.formLayout.itemAt(x, QFormLayout.FieldRole)
            self.field_list.append(widget.widget())
            Lumberjack.debug('(__init__) - fieldlist add = {}'.format(widget.widget()))
            if hasattr(widget, 'amount'):
                Lumberjack.debug('(__init__) - widget with amount attr.')
            if widget == self.balanceCurrencyEdit:
                Lumberjack.debug('(__init__) - widget is self.balanceCurrencyEdit')

        self.titleLabel.setText('Bank accounts')
        self.set_controls()
        self.set_mapper()

    def set_mapper(self):
        self.mapper.addMapping(self.bankNameLineEdit, 0)
        self.mapper.addMapping(self.userComboBox, 1)
        self.mapper.addMapping(self.accountLineEdit, 2)
        self.mapper.addMapping(self.balanceCurrencyEdit, 3)
        self.mapper.setCurrentIndex(0)

    def set_controls(self):
        session = self.dbhelper.get_app_db_session()
        user_model = AlchemicalTableModel(
            session,
            User,
            [('Full Name', User.fullname, 'fullname', {})])

        self.userComboBox.setModel(user_model)

        self.mapper.setCurrentIndex(0)
        self.toggle_edit_mode(False, None, None)


class ContractForm(BasicForm, Ui_ContractFormInsert):

    def __init__(self, *args):
        super(ContractForm, self).__init__(*args)
        Ui_ContractFormInsert.setupUi(self, self.FormContainer)
        Ui_ContractFormInsert.retranslateUi(self, self.FormContainer)
        self.setMaximumSize(QSize(450, 16777215))
        Lumberjack.info('evolving to a << ContractForm >>')

        for x in range(self.formLayout.rowCount()):
            widget = self.formLayout.itemAt(x, QFormLayout.FieldRole)
            self.field_list.append(widget.widget())

        self.titleLabel.setText('Contracts')
        self.set_controls()
        self.set_mapper()

    def set_mapper(self):
        Lumberjack.info('< ContractForm > - -> (set_mapper)')
        self.mapper.addMapping(self.relationComboBox, 0)
        self.mapper.addMapping(self.referenceLineEdit, 1)
        self.mapper.addMapping(self.userComboBox, 2)
        self.mapper.addMapping(self.accountComboBox, 3)
        self.mapper.addMapping(self.letterComboBox, 4)
        self.mapper.addMapping(self.emailComboBox, 5)
        self.mapper.addMapping(self.contractTypeComboBox, 6)
        self.mapper.addMapping(self.totalAmountCurrencyEdit, 7)
        self.mapper.addMapping(self.recurAmountCurrencyEdit, 8)
        self.mapper.addMapping(self.recurrenceBox, 9)
        self.mapper.addMapping(self.startDateDateEdit, 10)
        self.mapper.addMapping(self.endDateDateEdit, 11)
        self.mapper.setCurrentIndex(0)

    def set_controls(self):
        Lumberjack.info('< ContractForm > - -> (set_controls)')
        session = self.dbhelper.get_app_db_session()
        relation_model = AlchemicalTableModel(
            session,
            Relation,
            [('Name', Relation.name, 'name', {})])
        
        user_model = AlchemicalTableModel(
            session,
            User,
            [('Full Name', User.fullname, 'fullname', {})])

        account_model = AlchemicalTableModel(
            session,
            BankAccount,
            [('Account Nr.', BankAccount.account, 'account', {})])

        letter_model = AlchemicalTableModel(
            session,
            Letter,
            [('Reference', Letter.reference, 'reference', {})])

        email_model = AlchemicalTableModel(
            session,
            EmailAddress,
            [('Address', EmailAddress.address, 'address', {})])

        type_model = TypeModel(
            session,
            Type,
            [('Contract type', Type.contract, 'contract', {})])

        self.relationComboBox.setModel(relation_model)
        self.userComboBox.setModel(user_model)
        self.accountComboBox.setModel(account_model)
        self.letterComboBox.setModel(letter_model)
        self.emailComboBox.setModel(email_model)
        self.contractTypeComboBox.setModel(type_model)

        recurIcon = qta.icon('fa.refresh', color='white')
        self.recurrenceCheckBox.setIcon(recurIcon)
        self.recurrenceCheckBox.stateChanged.connect(self.on_recurrence)
        self.recurrenceBox.valueSet.connect(self.set_checkbox)

        self.toggle_edit_mode(False, None, None)

    def on_recurrence(self):
        Lumberjack.info('< ContractForm > - -> (on_recurrence)')
        if self.recurrenceCheckBox.isChecked():
            self.formLayout.insertRow(12, self.repeatLabel, self.recurrenceBox)
            self.formLayout.insertRow(13, self.recurAmountLabel, self.recurAmountCurrencyEdit)
            self.repeatLabel.show()
            self.recurrenceBox.show()
            self.recurAmountLabel.show()
            self.recurAmountCurrencyEdit.show()
        else:
            self.repeatLabel.hide()
            self.formLayout.removeWidget(self.repeatLabel)
            self.recurrenceBox.hide()
            self.formLayout.removeWidget(self.recurrenceBox)
            self.recurAmountLabel.hide()
            self.formLayout.removeWidget(self.recurAmountLabel)
            self.recurAmountCurrencyEdit.hide()
            self.formLayout.removeWidget(self.recurAmountCurrencyEdit)
            if self.recurrenceBox.recurrenceValue is not None:
                self.recurrenceBox.recurrenceValue = None
            if self.recurAmountCurrencyEdit.amount is not None:
                self.recurAmountCurrencyEdit.amount = None

    def set_checkbox(self, *args):
        Lumberjack.info('< ContractForm > - -> (set_checkbox)')
        Lumberjack.info('(set_checkbox) - args = {}'.format(args))
        if args[0]:
            self.recurrenceCheckBox.setCheckState(Qt.Checked)
        else:
            self.recurrenceCheckBox.setCheckState(Qt.Unchecked)
        self.on_recurrence()

class EmailAddressForm(BasicForm, Ui_EmailAddressFormInsert):

    def __init__(self, *args):
        super(EmailAddressForm, self).__init__(*args)
        Ui_EmailAddressFormInsert.setupUi(self, self.FormContainer)
        Ui_EmailAddressFormInsert.retranslateUi(self, self.FormContainer)

        for x in range(self.formLayout.rowCount()):
            widget = self.formLayout.itemAt(x, QFormLayout.FieldRole)
            self.field_list.append(widget.widget())

        self.titleLabel.setText('Email addresses')
        self.set_controls()
        self.set_mapper()

    def set_mapper(self):
        self.mapper.addMapping(self.userComboBox, 0)
        self.mapper.addMapping(self.addressLineEdit, 1)
        self.mapper.setCurrentIndex(0)

    def set_controls(self):
        session = self.dbhelper.get_app_db_session()
        user_model = AlchemicalTableModel(
            session,
            User,
            [('Full Name', User.fullname, 'fullname', {})])

        self.userComboBox.setModel(user_model)

        self.mapper.setCurrentIndex(0)
        self.toggle_edit_mode(False, None, None)


class LetterForm(BasicForm, Ui_LetterFormInsert):

    def __init__(self, *args):
        super(LetterForm, self).__init__(*args)
        if self.mapper:
            print(Fore.CYAN + 'Mapper exists: ', self.mapper)
        Ui_LetterFormInsert.setupUi(self, self.FormContainer)
        Ui_LetterFormInsert.retranslateUi(self, self.FormContainer)

        for x in range(self.formLayout.rowCount()):
            widget = self.formLayout.itemAt(x, QFormLayout.FieldRole)
            self.field_list.append(widget.widget())

        self.titleLabel.setText('Letters')
        self.set_controls()
        self.set_mapper()

    def set_mapper(self):
        self.mapper.addMapping(self.dateDateEdit, 0)
        self.mapper.addMapping(self.subjectLineEdit, 1)
        self.mapper.addMapping(self.senderComboBox, 2)
        self.mapper.addMapping(self.referenceLineEdit, 3)
        self.mapper.addMapping(self.userComboBox, 4)
        self.mapper.addMapping(self.scanFileDrop, 5)
        self.mapper.addMapping(self.typeComboBox, 6)
        self.mapper.setCurrentIndex(0)

    def set_controls(self):
        session = self.dbhelper.get_app_db_session()
        user_model = AlchemicalTableModel(
            session,
            User,
            [('Full Name', User.fullname, 'fullname', {})])

        relation_model = AlchemicalTableModel(
            session,
            Relation,
            [('Name', Relation.name, 'name', {})])

        type_model = TypeModel(
            session,
            Type,
            [('Letter type', Type.letter, 'letter', {})])

        self.userComboBox.setModel(user_model)
        self.senderComboBox.setModel(relation_model)
        self.typeComboBox.setModel(type_model)
        self.toggle_edit_mode(False, None, None)

    def save_check(self):
        print('Scanning for file in db protocol.')
        mapper_file_name = self.scanFileDrop.getCurrentFile()
        print('Mapper file name = ', mapper_file_name)
        print('with type = ', type(mapper_file_name))
        projection_dir = str(self.senderComboBox.currentItem.name)
        projection_name = '{date}_{sender}_{reference}.pdf'.format(
            date=self.dateDateEdit.date().toPyDate(),
            sender=self.senderComboBox.currentItem.name,
            reference=self.referenceLineEdit.text())
        print('File Projection = ', (projection_dir, projection_name))
        stored_file = DbFileHandler().store_file(mapper_file_name, (projection_dir, projection_name))
        print('stored file = ', stored_file)
        print('with type = ', type(stored_file))
        self.scanFileDrop.setCurrentFile(stored_file)


class RelationForm(BasicForm, Ui_RelationFormInsert):

    def __init__(self, *args):
        super(RelationForm, self).__init__(*args)
        if self.mapper:
            print(Fore.CYAN + 'Mapper exists: ', self.mapper)
        Ui_RelationFormInsert.setupUi(self, self.FormContainer)
        Ui_RelationFormInsert.retranslateUi(self, self.FormContainer)

        for x in range(self.formLayout.rowCount()):
            widget = self.formLayout.itemAt(x, QFormLayout.FieldRole)
            self.field_list.append(widget.widget())

        self.titleLabel.setText('Relations')
        self.set_controls()
        self.set_mapper()

    def set_mapper(self):
        self.mapper.addMapping(self.nameLineEdit, 0)
        self.mapper.addMapping(self.fullNameLineEdit, 1)
        self.mapper.addMapping(self.referenceLineEdit, 2)
        self.mapper.addMapping(self.bankAccountLineEdit, 3)
        self.mapper.addMapping(self.typeComboBox, 4)
        self.mapper.setCurrentIndex(0)

    def set_controls(self):
        session = self.dbhelper.get_app_db_session()
        type_model = TypeModel(
            session,
            Type,
            [('Relation', Type.relation, 'relation', {})])

        self.typeComboBox.setModel(type_model)

        self.mapper.setCurrentIndex(0)
        self.toggle_edit_mode(False, None, None)


class TransactionForm(BasicForm, Ui_TransactionFormInsert):

    def __init__(self, *args):
        super(TransactionForm, self).__init__(*args)
        Ui_TransactionFormInsert.setupUi(self, self.FormContainer)
        Ui_TransactionFormInsert.retranslateUi(self, self.FormContainer)

        for x in range(self.formLayout.rowCount()):
            widget = self.formLayout.itemAt(x, QFormLayout.FieldRole)
            self.field_list.append(widget.widget())

        self.titleLabel.setText('Transactions')
        self.set_controls()
        self.set_mapper()

    def set_mapper(self):
        self.mapper.addMapping(self.contractComboBox, 0)
        self.mapper.addMapping(self.letterComboBox, 1)
        self.mapper.addMapping(self.accountComboBox, 2)
        self.mapper.addMapping(self.amountLineEdit, 3)
        self.mapper.addMapping(self.transactionDateEdit, 4)
        self.mapper.addMapping(self.paymentDateEdit, 5)
        self.mapper.addMapping(self.paymentStateCheckBox, 6)
        self.mapper.addMapping(self.debitCheckBox, 7)
        self.mapper.setCurrentIndex(0)
        
    def set_controls(self):
        session = self.dbhelper.get_app_db_session()        
        contract_model = AlchemicalTableModel(
            session,
            Contract,
            [('Reference', Contract.reference, 'reference', {})])

        letter_model = AlchemicalTableModel(
            session,
            Letter,
            [('Reference', Letter.reference, 'reference', {})])

        account_model = AlchemicalTableModel(
            session,
            BankAccount,
            [('Account Nr.', BankAccount.account, 'account', {})])

        self.contractComboBox.setModel(contract_model)
        self.letterComboBox.setModel(letter_model)
        self.accountComboBox.setModel(account_model)

        self.mapper.setCurrentIndex(0)
        self.toggle_edit_mode(False, None, None)


class UserForm(BasicForm, Ui_UserFormInsert):

    def __init__(self, *args):
        super(UserForm, self).__init__(*args)
        Ui_UserFormInsert.setupUi(self, self.FormContainer)
        Ui_UserFormInsert.retranslateUi(self, self.FormContainer)

        for x in range(self.formLayout.rowCount()):
            widget = self.formLayout.itemAt(x, QFormLayout.FieldRole)
            self.field_list.append(widget.widget())

        self.titleLabel.setText('Users')
        self.set_controls()
        self.set_mapper()

    def set_mapper(self):
        self.mapper.addMapping(self.nameLineEdit, 0)
        self.mapper.addMapping(self.fullnameLineEdit, 1)
        self.mapper.addMapping(self.passwordLineEdit, 2)
        self.mapper.setCurrentIndex(0)
        
    def set_controls(self):
        self.mapper.setCurrentIndex(0)
        self.toggle_edit_mode(False, None, None)

