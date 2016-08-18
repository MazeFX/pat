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

FORMS    += letter_form.ui \
    ui/letter_form.ui \
    ui/login_dialog.ui \
    ui/mainwindow.ui \
    ui/main_window.ui \
    ui/letter_tab.ui \
    ui/settings_dialog.ui \
    ui/home_tab.ui \
    ui/save_dialog.ui

DISTFILES += \
    __pycache__/ui_letter_form.cpython-35.pyc \
    ui_letter_form.py \
    ui/MyCustom.py \
    ui/test.py

PYQTDESIGNERPATH = custom_widget_plugin
