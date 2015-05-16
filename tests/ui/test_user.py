import os
from app import create_app
from app.config import TestConfiguration
from app.extensions import db
from app.models import User
from flask.ext.testing import LiveServerTestCase
from selenium import webdriver

class LiveServerTestBase(LiveServerTestCase):
    def create_app(self):
        self.app = create_app(TestConfiguration)
        return self.app

    def init_data(self):
        db.create_all()
        User.create(username='gary', password='password')

    def setUp(self):
        self.init_data()
        self.browser = webdriver.Chrome()

    def tearDown(self):
        db.drop_all()
        os.unlink(self.app.config['DATABASE'])
        self.browser.quit()

    def test_dumb(self):
        self.browser.get(self.get_server_url() + '/user/login')

    def test_login(self):
        self.browser.get(self.get_server_url() + '/user/login')
        name_form = self.browser.find_element_by_id('name')
        pwd_form = self.browser.find_element_by_id('password')
        submit_form = self.browser.find_element_by_id('submit')
        name_form.send_keys('gary')
        pwd_form.send_keys('password')
        submit_form.click()

        self.assertIn('Login successful', self.browser.page_source)