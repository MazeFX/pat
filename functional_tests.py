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
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

from forms import LetterForm

app = QApplication(sys.argv)


class LetterTest(unittest.TestCase):
    """Test the gui for letter functions"""

    def setUp(self):
        self.form = LetterForm()
        pass

    def tearDown(self):
        pass

    def test_user_can_add_a_new_letter(self):
        # User wants to add a new letter to the database
        # User enters the letter attributes
        letter_date_input = self.form.letter_date_input

        self.fail('Finish the Test!')


if __name__ == "__main__":
    unittest.main()

