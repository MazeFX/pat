# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: qvariantalchemy.py
Creator: MazeFX
Date: 8-8-2016

Python Test docstring.
"""

import datetime
from decimal import Decimal

from PyQt5.QtCore import QVariant, QDate
from sqlalchemy import types


def gen_process_bind_param(pytype, toqtype, self, value, dialect):
    print('--------- From gen_proces_bind :  -------------')
    print('-value = ', value)
    if value is None:
        return None
    elif isinstance(value, QVariant):
        print('-value is instance Qvariant = ', value)
        print('-return value = ', pytype(toqtype(value)))
        print('-return type = ', type(pytype(toqtype(value))))
        return pytype(toqtype(value))
    elif isinstance(value, QDate):
        print('-value is instance QDate = ', value)
        print('-return value = ', value.toPyDate())
        print('-return type = ', type(value.toPyDate()))
        return value.toPyDate()
    elif not isinstance(value, pytype):
        print('-value not is instance pytype = ', value)

        return pytype(value)
    else:
        print('-value unchanged return = ', value)
        return value


class Integer(types.TypeDecorator):
    impl = types.Integer

    def process_bind_param(self, value, dialect):
        return gen_process_bind_param(
            int, lambda value: value.toLongLong(),
            self, value, dialect)


class Numeric(types.TypeDecorator):
    impl = types.Numeric

    def process_bind_param(self, value, dialect):
        print('--------- From Numeric type:  -------------')
        print('-value = ', value)
        return gen_process_bind_param(
            int, lambda value: round(Decimal(value), 2),
            self, value, dialect)


class Boolean(types.TypeDecorator):
    impl = types.Boolean

    def process_bind_param(self, value, dialect):
        return gen_process_bind_param(
            bool, lambda value: value.toBool(),
            self, value, dialect)


class String(types.TypeDecorator):
    impl = types.Unicode

    def process_bind_param(self, value, dialect):
        return gen_process_bind_param(
            str, lambda value: value.toString(),
            self, value, dialect)


class Enum(types.TypeDecorator):
    impl = types.Enum

    def process_bind_param(self, value, dialect):
        return gen_process_bind_param(
            str, lambda value: value.toString(),
            self, value, dialect)


class Date(types.TypeDecorator):
    impl = types.Date

    def process_bind_param(self, value, dialect):
        print('--------- From Date type:  -------------')
        print('-value = ', value)
        return gen_process_bind_param(
            datetime.date, lambda value: value.toPyDate(),
            self, value, dialect)


class DateTime(types.DateTime):
    impl = types.DateTime

    def process_bind_param(self, value, dialect):
        return gen_process_bind_param(
            datetime.datetime, lambda value: value.toDateTime(),
            self, value, dialect)
