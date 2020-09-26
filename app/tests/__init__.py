import os
import unittest
from app import create_app
from app.extensions.database import db


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['DEBUG'] = True
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_TESTING')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def headers(self):
        data = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        return data