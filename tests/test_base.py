from app import create_app
from app.config import TestConfiguration
from flask.ext.testing import TestCase

from app.extensions import db


class BaseTestCase(TestCase):
    """
    Classes that inherit this class are able to test with the config.TestConfiguration setup that is provided in
    config.py.
    """

    def create_app(self):
        return create_app(TestConfiguration)

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
