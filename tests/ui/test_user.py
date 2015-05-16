from time import sleep
import unittest

from app import create_app
from app.config import TestConfiguration
from app.extensions import db
from app.models import User

from flask import url_for
from flask.ext.testing import TestCase
from selenium import webdriver


class UserUITest(TestCase):
    """
    Classes that inherit this class are able to test with the config.TestConfiguration setup that is provided in
    config.py.
    """

    def create_app(self):
        self.app = create_app(TestConfiguration)
        return self.app

    def setUp(self):
        self._ctx = self.app.test_request_context()
        self._ctx.push()
        self.browser = webdriver.Chrome()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.browser.quit()
        self._ctx.pop()

    def login(self, username, password):
        data = {
            'name': username,
            'password': password,
        }
        response = self.client.post('/login', data=data, follow_redirects=True)
        assert "Hello" in response.data
        return response

    def _login(self, userstr, passstr):
        self.browser.get(self.get_server_url() + url_for("user.login"))
        name = self.browser.find_element_by_id("name")
        password = self.browser.find_element_by_id("password")
        submit = self.browser.find_element_by_id("submit")

        name.send_keys(userstr)
        password.send_keys(passstr)
        submit.click()

    def test_url_for_user_login_works(self):
        self.assertEqual(url_for('user.login'), "/user/login/")

    def test_login_form_appears_in_user_login(self):
        self.browser.get("http://localhost:5001" + url_for('user.login'))
        self.assertIn("Username", self.browser.page_source)
        self.assertIn("Password", self.browser.page_source)

    def test_successful_login_works(self):
        User.create(username='gary', password='password')
        self.login('gary', 'password')
        sleep(100)
        self.assertIn('gary', self.browser.page_source)




if __name__ == '__main__':
    unittest.main()
