# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: forms.py
Creator: MazeFX
Date: 1-8-2016

Python Test docstring.
"""
from PyQt5.QtCore import Qt, QDate, QModelIndex
from PyQt5.QtWidgets import QWidget, QDataWidgetMapper

from db.models import AlchemicalTableModel, User, Relation
from db.helper import DbHelper, DbFileHandler
from MyQtness.ui_letter_form import Ui_LetterForm
from MyQtness.ui_relation_form import Ui_RelationForm
from MyQtness.ui_user_form import Ui_UserForm
from MyQtness.myWidgets import MyItemDelegate
from dialogs import SaveDialog

from colorama import Fore, Back, Style


class LetterForm(QWidget, Ui_LetterForm):

    dbhelper = None

    def __init__(self, *kwargs):
        super(LetterForm, self).__init__(*kwargs)

        self.setupUi(self)
        self.edit_mode = None

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

    def setModel(self, model):
        self.model = model

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.dateDateEdit, 0)
        self.mapper.addMapping(self.subjectLineEdit, 1)
        self.mapper.addMapping(self.senderComboBox, 2)
        self.mapper.addMapping(self.referenceLineEdit, 3)
        self.mapper.addMapping(self.userComboBox, 4)
        self.mapper.addMapping(self.scanFileDrop, 5)
        self.mapper.setCurrentIndex(0)

        delegate = MyItemDelegate(self)
        self.mapper.setItemDelegate(delegate)
        self.set_controls()

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
        self.dateDateEdit.setEnabled(flag)
        self.subjectLineEdit.setEnabled(flag)
        self.senderComboBox.setEnabled(flag)
        self.referenceLineEdit.setEnabled(flag)
        self.userComboBox.setEnabled(flag)
        self.scanFileDrop.edit = flag

    def set_mapper_index_from_selection(self, *args):
        print('Setting letter form mapper index: ', args)
        if self.edit_mode:
            self.toggle_edit_mode(False, None, None)

        selected_index = args[0].indexes()
        row_index = selected_index[0].row()
        self.mapper.setCurrentIndex(row_index)
        print('Setting letter form mapper index: ', row_index)

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
        now = QDate.currentDate()
        self.dateDateEdit.setDate(now)
        self.subjectLineEdit.setFocus()
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
        self.check_scanned_file()
        if self.edit_mode == 'add':
            self.model.storeRow(self.newRow)
            # TODO - Check sql insert unnecessary
            self.mapper.submit()
            self.NewRow = None
        if self.edit_mode == 'edit':
            self.mapper.submit()
        self.toggle_edit_mode(False, None, None)

    def check_scanned_file(self):
        print('Scanning for file in db protocol.')
        mapper_file_name = self.scanFileDrop.getCurrentFile()
        print('Mapper file name = ', mapper_file_name)
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


class UserForm(QWidget, Ui_UserForm):

    dbhelper = None

    def __init__(self, *kwargs):
        super(UserForm, self).__init__(*kwargs)

        self.setupUi(self)
        self.edit_mode = None

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

    def setModel(self, model):
        self.model = model

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.nameLineEdit, 0)
        self.mapper.addMapping(self.fullnameLineEdit, 1)
        self.mapper.addMapping(self.passwordLineEdit, 2)

        delegate = MyItemDelegate(self)
        self.mapper.setItemDelegate(delegate)
        self.mapper.setCurrentIndex(0)

        self.toggle_edit_mode(False, None, None)

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
        self.nameLineEdit.setEnabled(flag)
        self.fullnameLineEdit.setEnabled(flag)
        self.passwordLineEdit.setEnabled(flag)

    def set_mapper_index_from_selection(self, *args):
        print('Setting letter form mapper index: ', args)
        if self.edit_mode:
            self.toggle_edit_mode(False, None, None)

        selected_index = args[0].indexes()
        row_index = selected_index[0].row()
        self.mapper.setCurrentIndex(row_index)
        print('Setting letter form mapper index: ', row_index)

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

        self.nameLineEdit.setFocus()
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
        self.check_scanned_file()
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



class RelationForm(QWidget, Ui_RelationForm):

    dbhelper = None

    def __init__(self, *kwargs):
        super(RelationForm, self).__init__(*kwargs)

        self.setupUi(self)
        self.edit_mode = None

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

    def setModel(self, model):
        self.model = model

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.nameLineEdit, 0)
        self.mapper.addMapping(self.fullNameLineEdit, 1)
        self.mapper.addMapping(self.referenceLineEdit, 2)
        self.mapper.addMapping(self.bankAccountLineEdit, 3)
        self.mapper.addMapping(self.typeComboBox, 4)
        self.mapper.addMapping(self.startDateEdit, 5)
        self.mapper.addMapping(self.endDateEdit, 6)

        delegate = MyItemDelegate(self)
        self.mapper.setItemDelegate(delegate)
        self.mapper.setCurrentIndex(0)

        self.toggle_edit_mode(False, None, None)

        #self.set_controls()

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

        self.nameLineEdit.setEnabled(flag)
        self.fullNameLineEdit.setEnabled(flag)
        self.referenceLineEdit.setEnabled(flag)
        self.bankAccountLineEdit.setEnabled(flag)
        self.typeComboBox.setEnabled(flag)
        self.startDateEdit.setEnabled(flag)
        self.endDateEdit.setEnabled(flag)

    def set_mapper_index_from_selection(self, *args):
        print('Setting letter form mapper index: ', args)
        if self.edit_mode:
            self.toggle_edit_mode(False, None, None)

        selected_index = args[0].indexes()
        row_index = selected_index[0].row()
        self.mapper.setCurrentIndex(row_index)
        print('Setting letter form mapper index: ', row_index)

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
        now = QDate.currentDate()
        self.startDateEdit.setDate(now)
        self.endDateEdit.setDate(now)
        self.subjectLineEdit.setFocus()
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
        self.check_scanned_file()
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
