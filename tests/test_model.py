import unittest

from tests.models.test_follow import FollowTest


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(FollowTest))
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
