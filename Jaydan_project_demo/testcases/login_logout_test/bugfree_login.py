# -*- coding:utf-8 -*-  
# author:Jaydan

import unittest
from selenium import webdriver

from testcases.common_logic.common import *
from config import *

class LoginTest(unittest.TestCase):

    def setup(self):
        self.executable_path = chrome_driver
        self.driver = webdriver.Chrome(executable_path=self.executable_path)
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.url = "http://localhost/bugfree"
        open_url(self.driver, self.url)
        bugfree_login(self.driver, "admin", "111111")

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        self.assertTrue(True)





