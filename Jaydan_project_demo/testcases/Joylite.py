#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from time import sleep
import unittest
from appium import webdriver
from testcases.common_logic.common import *

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SelectCam(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities())
        drivers = self.driver

    def tearDown(self):
        # end the session
        self.driver.quit()
    def test_new_cams(self):
        sleep(2)
        el = self.driver.find_elements_by_class_name('android.widget.ImageView')  #点击添加按钮
        el[0].click()
        add_new = self.driver.find_elements_by_class_name("android.widget.TextView")
        self.assertEqual(u"添加新的摄像机", add_new[0].text)
        print add_new[0].text
    def test_friends_cams(self):
        sleep(2)
        el = self.driver.find_elements_by_class_name('android.widget.ImageView')  # 点击添加按钮
        el[0].click()
        add_new = self.driver.find_elements_by_class_name("android.widget.TextView")
        self.assertEqual(u"添加新的摄像机", add_new[0].text)
        print add_new[0].text
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
