from unittest import TestCase
from app import app
import json
import base_test

class TestHome(TestCase):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/')

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()),{'message': 'Hello, world!'}
            ) 