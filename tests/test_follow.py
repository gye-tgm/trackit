import unittest
from app.models import User, Follow
from tests.test_base import BaseTestCase


class MyTestCase(BaseTestCase):
    def test_following(self):
        u1 = User.create(username='gary')
        u2 = User.create(username='admin')
        u3 = User.create(username='bad')

        f1 = Follow.create(b=u2)
        u1.following.append(f1)
        f2 = Follow.create(b=u3)
        u1.following.append(f2)

        print(u1.following)

        exp = [u2, u3]
        self.assertEqual(u1.get_following(), exp)

    def test_followers(self):
        u1 = User.create(username='gary')
        u2 = User.create(username='admin')
        u3 = User.create(username='bad')

        f2 = Follow.create(b=u2)
        u1.following.append(f2)
        f2 = Follow.create(b=u2)
        u3.following.append(f2)

        u1.save()
        u3.save()

        exp = [u1, u3]
        self.assertEqual(u2.get_followers(), exp)




if __name__ == '__main__':
    unittest.main()
