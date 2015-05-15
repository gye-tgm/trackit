import unittest

from app.models import User, TwitterAccount, FacebookAccount
from tests.test_base import BaseTestCase


class UserTest(BaseTestCase):
    def test_get_users(self):
        u = User.create(username='joe')
        t = TwitterAccount(username='joe')
        f = FacebookAccount(url='http://fb.com')
        u.accounts.append(t)
        u.accounts.append(f)
        u.save()

        exp = [t]
        self.assertTrue(u.get_twitter_accounts(), exp)


if __name__ == '__main__':
    unittest.main()
