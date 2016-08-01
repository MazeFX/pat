# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: functional_tests.py
Creator: MazeFX
Date: 1-8-2016

Functional test for testing P.A.T. functions

Test overview:
--------------

* Letters - User can add letters to the database

"""

__author__ = "MazeFX"
__version__ = "$Version 0.1 $"
__date__ = "$Date: 2016-08-01 $"
__copyright__ = "Copyright 2016 MazeFX Solutions"

import sys
import unittest
from PyQt5.QtGui import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)


class LetterTest(unittest.TestCase):
    """Test the gui for letter functions"""

    def setUp(self):
        pass

    def test_user_can_a_new_letter(self):
        pass


if __name__ == "__main__":
    unittest.main()

