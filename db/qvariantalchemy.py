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

from PyQt5.QtCore import QVariant
from sqlalchemy import types


def gen_process_bind_param(pytype, toqtype, self, value, dialect):
    if value is None:
        return None
    elif isinstance(value, QVariant):
        return pytype(toqtype(value))
    elif not isinstance(value, pytype):
        return pytype(value)
    else:
        return value


class Integer(types.TypeDecorator):
    impl = types.Integer

    def process_bind_param(self, value, dialect):
        return gen_process_bind_param(
            int, lambda value: value.toLongLong(),
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


class Date(types.Date):
    impl = types.Date

    def process_bind_param(self, value, dialect):
        return gen_process_bind_param(
            datetime.date, lambda value: value.toPyDate(),
            self, value, dialect)


class DateTime(types.DateTime):
    impl = types.DateTime

    def process_bind_param(self, value, dialect):
        return gen_process_bind_param(
            datetime.datetime, lambda value: value.toDateTime(),
            self, value, dialect)
