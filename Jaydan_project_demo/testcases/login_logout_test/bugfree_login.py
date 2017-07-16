# -*- coding:utf-8 -*-  
# author:Jaydan

import unittest
from selenium import webdriver
from testcases.common_logic import *

class LoginTest(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.url = "http://localhost/bugfree"
        open_url(self.driver,self.url)
        bugfree_login(self.driver,"admin","123456")
