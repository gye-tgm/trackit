from time import sleep
from app import create_app
from app.config import TestConfiguration
from app.extensions import db
from app.models import User

from flask.ext.testing import TestCase as Base


class TestCase(Base):
    """Base TestClass for your application."""

    def create_app(self):
        """Create and return a testing flask app."""

        app = create_app(TestConfiguration)
        return app

    def init_data(self):
        User.create(username='gary', password='password')

    def setUp(self):
        db.create_all()
        self.init_data()

    def tearDown(self):
        db.drop_all()

    def login(self, username, password):
        data = {
            'name': username,
            'password': password,
        }
        response = self.client.post('/users/login', data=data, follow_redirects=True)
        print(response.data)
        self.assertIn("Howdy", str(response.data))
        return response

    def _logout(self):
        response = self.client.get('/users/logout')
        self.assertRedirects(response, location='/')

    def _test_get_request(self, endpoint, template=None):
        response = self.client.get(endpoint)
        self.assert_200(response)
        if template:
            self.assertTemplateUsed(name=template)
        return response


class TestFrontend(TestCase):
    def test_login(self):
        sleep(100)
        self.login('gary', 'password')


