"""
This file holds the tests for db.py.
"""

from unittest import TestCase, skip
# import random

from db import db


class DBTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_users(self):
        """
        Can we fetch user db?
        """
        users = db.get_users()
        self.assertIsInstance(users, dict)

    def test_active_subscription(self, username):
        """
        Can we fetch active subscriptions?
        """
        active_subs = db.get_active_subs(username)
        self.assertIsInstance(active_subs, dict)
    
    def test_inactive_subscription(self, username):
        """
        Can we fetch inactive subscriptions?
        """
        inactive_subs = db.get_inactive_subs(username)
        self.assertIsInstance(inactive_subs, dict)