# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: hook-qtawesome.py
Creator: MazeFX
Date: 7-9-2016

Pyinstaller hook file for Qt Awesome module.
Needed for module .json files.
"""

from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('qtawesome')
