from app.models import User, TwitterAccount, FacebookAccount
from flask import url_for
from flask.ext.login import current_user
from tests.test_base import BaseTestCase


class UserViewsTests(BaseTestCase):
    def test_users_can_login(self):
        """
        Creates a user, tries to login and checks whether login is ok.
        """
        User.create(username='joe', password='12345')
        response = self.client.post(url_for('users.login'), data={'name': 'joe', 'password': '12345'})
        self.assert_redirects(response, url_for('users.index'))

    def test_users_can_logout(self):
        User.create(username='joe', password='12345')

        with self.client:
            self.client.post(url_for('users.login'), data={'name': 'joe', 'password': '12345'})
            self.client.get(url_for("users.logout"))
            self.assertTrue(current_user.is_anonymous())

    def test_get_users(self):
        u = User.create(username='joe')
        t = TwitterAccount(username='joe')
        f = FacebookAccount(url='http://fb.com')
        u.accounts.append(t)
        u.accounts.append(f)
        u.save()

        exp = [t]
        self.assertTrue(u.get_twitter_accounts(), exp)