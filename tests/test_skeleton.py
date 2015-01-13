"""
Base test skeleton.
"""

import os
import sys
import unittest

from app import app, db

class TestSkeleton(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config.from_pyfile('../tests/test_config.py')
        cls.test_app = app.test_client()
        cls.test_db = db

    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.test_db.create_all()

    def tearDown(self):
        self.test_db.session.remove()
        self.test_db.drop_all()
