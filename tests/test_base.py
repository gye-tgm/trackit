from app import create_app
from flask.ext.testing import TestCase

from app.extensions import db


class BaseTestCase(TestCase):
    def create_app(self):
        return create_app('config.TestConfiguration')

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()