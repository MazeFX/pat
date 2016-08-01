# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: __init__.py
Creator: MazeFX
Date: 1-8-2016

Python Test docstring.
"""

import os.path
import traceback
import importlib

from PyQt5.QtCore import QFile, QTextStream

version = 1.0


def get_style(style_sheet):
    try:
        f = QFile(os.path.join(os.path.dirname(__file__), '{}.qss'.format(style_sheet)))
        f.open(QFile.ReadOnly | QFile.Text)
        ts = QTextStream(f)
        stylesheet = ts.readAll()
    except Exception as e:
        print(
            "Style sheet available, but an error occured...")
        traceback.print_exc()
        return u""

    return stylesheet
