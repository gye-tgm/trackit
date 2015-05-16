from app.models import User
from flask import url_for
from flask.ext.login import current_user
from tests.test_base import BaseTestCase


class UserViewsTests(BaseTestCase):
    def test_users_can_login(self):
        User.create(username='joe', password='12345')
        response = self.client.post(url_for('user.login'), data={'name': 'joe', 'password': '12345'})
        self.assert_redirects(response, url_for('user.index'))

    def test_users_can_logout(self):
        User.create(username='joe', password='12345')

        with self.client:
            self.client.post(url_for('user.login'), data={'name': 'joe', 'password': '12345'})
            self.client.get(url_for("user.logout"))
            self.assertTrue(current_user.is_anonymous())
