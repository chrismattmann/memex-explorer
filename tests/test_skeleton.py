"""
Base test skeleton.
"""

import os
import sys
import unittest

from app import app, db
from app.config import BASEDIR

TESTDB = os.path.join(BASEDIR, 'test_app.db')
TESTDB_SQLALCHEMY_DATABASE_URI = 'sqlite:///' + TESTDB 


class TestSkeleton(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = TESTDB_SQLALCHEMY_DATABASE_URI
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['TESTING'] = True
        app.port = 8943
        self.app = app.test_client()
        db.create_all()

        self.db = db

    def tearDown(self):
        os.remove(TESTDB)
