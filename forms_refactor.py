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
from PyQt5.QtWidgets import QApplication, QWidget, QDataWidgetMapper



from db.models import AlchemicalTableModel, User, Relation
from db.helper import DbHelper, DbFileHandler
from MyQtness.ui_basic_form import Ui_BasicForm
from MyQtness.ui_letter2_form import Ui_LetterForm
from MyQtness.ui_relation_form import Ui_RelationForm
from MyQtness.ui_user_form import Ui_UserForm
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
    field_list = []

    def __init__(self, *kwargs):
        super(BasicForm, self).__init__(*kwargs)

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

        #

        delegate = MyItemDelegate(self)
        self.mapper.setItemDelegate(delegate)
        self.mapper.setCurrentIndex(0)

        self.toggle_edit_mode(False, None, None)
        self.set_controls()

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
        self.dateDateEdit.setEnabled(flag)
        self.subjectLineEdit.setEnabled(flag)
        self.senderComboBox.setEnabled(flag)
        self.referenceLineEdit.setEnabled(flag)
        self.userComboBox.setEnabled(flag)
        self.scanFileDrop.edit = flag

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
        self.check_scanned_file()
        if self.edit_mode == 'add':
            self.model.storeRow(self.newRow)
            # TODO - Check sql insert unnecessary
            self.mapper.submit()
            self.NewRow = None
        if self.edit_mode == 'edit':
            self.mapper.submit()
        self.toggle_edit_mode(False, None, None)

    def on_reset(self):
        print(Fore.CYAN + 'Reset signal sent and recieved.')
        self.mapper.revert()


class LetterForm(BasicForm, Ui_LetterForm):

    def __init__(self, *kwargs):
        super(BasicForm, self).__init__(*kwargs)
        super(Ui_LetterForm, self).setupUi(self)

        self.setupUi(self)
        self.verticalLayout.insertWidget(3, self.formLayout)



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


def main():
    app = QApplication(sys.argv)

    w = LetterForm()
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
