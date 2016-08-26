#-------------------------------------------------
#
# Project created by QtCreator 2016-08-01T20:33:00
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = pat
TEMPLATE = app


SOURCES += main.cpp\
        letter_form.cpp

HEADERS  += letter_form.h

FORMS    += ui/basic_form.ui \
    ui/bank_account_form.ui \
    ui/contract_form.ui \
    ui/email_address_form.ui \
    ui/letter_form.ui \
    ui/relation_form.ui \
    ui/transaction_form.ui \
    ui/user_form.ui \
    ui/main_window.ui \
    ui/login_dialog.ui \
    ui/home_tab.ui \
    ui/settings_dialog.ui \
    ui/save_dialog.ui \
    ui/close_dialog.ui \

DISTFILES += \
    __pycache__/ui_letter_form.cpython-35.pyc \
    ui_letter_form.py \
    ui/MyCustom.py \
    ui/test.py

PYQTDESIGNERPATH = custom_widget_plugin
