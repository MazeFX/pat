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

from PyQt5.QtCore import QCoreApplication, Qt, QDate, QModelIndex
from PyQt5.QtWidgets import QApplication, QWidget, QDataWidgetMapper, QPushButton, QFormLayout

from db.models import AlchemicalTableModel, BankAccount, EmailAddress, Letter, Relation, Type, User
from db.helper import DbHelper, DbFileHandler

from MyQtness.ui_basic_form import Ui_BasicForm
from MyQtness.ui_bank_account_form import Ui_BankAccountFormInsert
from MyQtness.ui_contract_form import Ui_ContractFormInsert
from MyQtness.ui_email_address_form import Ui_EmailAddressFormInsert
from MyQtness.ui_letter_form import Ui_LetterFormInsert
from MyQtness.ui_relation_form import Ui_RelationFormInsert
from MyQtness.ui_bank_account_form import Ui_BankAccountFormInsert
from MyQtness.ui_user_form import Ui_UserFormInsert
from MyQtness.ui_transaction_form import Ui_TransactionFormInsert
from MyQtness.myWidgets import MyItemDelegate
from dialogs import SaveDialog

from colorama import Fore, Back, Style


class BasicForm(QWidget, Ui_BasicForm):
    '''
    Basic form class for creating tab forms.
    Class is not to be used. Use form class inhereting
    from this class.
    '''

    dbhelper = None
    model = None
    field_list = []

    def __init__(self, model, db_helper, *args):
        super(BasicForm, self).__init__(*args)

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

        self.pushButtonReset.setFocusPolicy(Qt.NoFocus)
        self.pushButtonReset.clicked.connect(self.on_reset)

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        print(Fore.CYAN + 'mapper created: ', self.mapper)
        delegate = MyItemDelegate(self)
        self.mapper.setItemDelegate(delegate)

        self.mapper.setModel(self.model)

    def set_mapper(self):
        pass

    def set_mapper_index_from_selection(self, *args):
        print('Setting letter form mapper index: ', args)
        if self.edit_mode:
            self.toggle_edit_mode(False, None, None)

        selected_index = args[0].indexes()
        row_index = selected_index[0].row()
        self.mapper.setCurrentIndex(row_index)
        print('Setting letter form mapper index: ', row_index)

    def set_controls(self):
        pass

    def toggle_edit_mode(self, flag, mode, row):
        print(Fore.CYAN + 'Setting edit mode for letter form: ', flag, mode)

        if flag and self.edit_mode is None:
            self.openItem = self.model.results[row]
            self.edit_mode = mode

        elif not flag and self.edit_mode:
            item_changed_saved = self.check_item_change()
            print(Fore.CYAN + 'Item Change saved: ', item_changed_saved)
            if item_changed_saved:
                self.openItem = None
            elif item_changed_saved is None:
                return
            else:
                self.on_reset()
                if self.edit_mode == 'add':
                    self.model.rollback_row(self.newRow)
                    self.newRow = None

        self.edit_mode = mode
        for field in self.field_list:
            if hasattr(field, 'edit'):
                field.edit = flag
            else:
                field.setEnabled(flag)

    def on_add(self):
        # TODO - when adding new item remove current list selection
        print(Fore.CYAN + 'Add signal sent and recieved.')
        row = self.model.rowCount(None)
        self.newRow = row
        self.model.insertRow(row)
        print(Fore.CYAN + 'Row count after add: ', self.model.rowCount(None))
        self.mapper.setCurrentIndex(row)
        print(Fore.CYAN + 'New row at index: ', row)
        print(Fore.CYAN + 'mapper index: ', self.mapper.currentIndex())
        self.toggle_edit_mode(True, 'add', row)
        print(Fore.CYAN + 'New row at index: ', row)
        print(Fore.CYAN + 'mapper index: ', self.mapper.currentIndex())

    def on_edit(self):
        print(Fore.CYAN + 'Edit signal sent and recieved.')
        print(Fore.CYAN + 'mapper index: ', self.mapper.currentIndex())
        if self.edit_mode in ('add', 'edit'):
            self.toggle_edit_mode(False, None, None)
        elif self.mapper.currentIndex() >= 0:
            self.toggle_edit_mode(True, 'edit', self.mapper.currentIndex())

    def on_delete(self):
        print(Fore.CYAN + 'Delete signal sent and recieved.')

    def on_save(self):
        print(Fore.CYAN + 'Save signal sent and recieved.')
        if hasattr(self, 'save_check'):
            print(Fore.CYAN + 'Checking for onsave checks.')
            self.save_check()
        if self.edit_mode == 'add':
            self.model.storeRow(self.newRow)
            # TODO - Check sql insert unnecessary
            self.mapper.submit()
            self.NewRow = None
        if self.edit_mode == 'edit':
            self.mapper.submit()
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

    def on_reset(self):
        print(Fore.CYAN + 'Reset signal sent and recieved.')
        self.mapper.revert()
        

class BankAccountForm(BasicForm, Ui_BankAccountFormInsert):

    def __init__(self, *args):
        super(BankAccountForm, self).__init__(*args)
        Ui_BankAccountFormInsert.setupUi(self, self.FormContainer)
        Ui_BankAccountFormInsert.retranslateUi(self, self.FormContainer)

        for x in range(self.formLayout.rowCount()):
            widget = self.formLayout.itemAt(x, QFormLayout.FieldRole)
            self.field_list.append(widget.widget())

        self.titleLabel.setText('Bank accounts')
        self.set_controls()
        self.set_mapper()

    def set_mapper(self):
        self.mapper.addMapping(self.bankNameLineEdit, 0)
        self.mapper.addMapping(self.userComboBox, 1)
        self.mapper.addMapping(self.accountComboBox, 2)
        self.mapper.addMapping(self.balanceLineEdit, 3)

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

        for x in range(self.formLayout.rowCount()):
            widget = self.formLayout.itemAt(x, QFormLayout.FieldRole)
            self.field_list.append(widget.widget())

        self.titleLabel.setText('Contracts')
        self.set_controls()
        self.set_mapper()

    def set_mapper(self):
        self.mapper.addMapping(self.relationComboBox, 0)
        self.mapper.addMapping(self.userComboBox, 1)
        self.mapper.addMapping(self.accountComboBox, 2)
        self.mapper.addMapping(self.letterComboBox, 3)
        self.mapper.addMapping(self.emailAddressComboBox, 4)
        self.mapper.addMapping(self.amountLineEdit, 5)
        self.mapper.addMapping(self.recurrenceBox, 6)
        self.mapper.addMapping(self.startDateDateEdit, 7)
        self.mapper.addMapping(self.endDateDateEdit, 8)

    def set_controls(self):
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

        self.relationComboBox.setModel(relation_model)
        self.userComboBox.setModel(user_model)
        self.accountComboBox.setModel(account_model)
        self.letterComboBox.setModel(letter_model)
        self.emailAddressComboBox.setModel(email_model)

        self.mapper.setCurrentIndex(0)
        self.toggle_edit_mode(False, None, None)


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

        self.userComboBox.setModel(user_model)
        self.senderComboBox.setModel(relation_model)
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
        self.mapper.addMapping(self.startDateEdit, 5)
        self.mapper.addMapping(self.endDateEdit, 6)

    def set_controls(self):
        session = self.dbhelper.get_app_db_session()
        type_model = AlchemicalTableModel(
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
        
    def set_controls(self):
        self.mapper.setCurrentIndex(0)
        self.toggle_edit_mode(False, None, None)

