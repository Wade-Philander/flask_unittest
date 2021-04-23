from unittest import TestCase
from app import app

class BaseTest(TestCase):
    def test_home(self):
        app.testing = True
        self.app = test_client