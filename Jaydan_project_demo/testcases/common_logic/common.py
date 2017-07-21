# -*- coding:utf-8 -*-
# author:Jaydan

import time

def open_url(driver,url):
    driver.get(url)

def bugfree_login(driver,username,password):
    driver.find_element_by_id("LoginForm_username").click()
    driver.find_element_by_id("LoginForm_username").send_keys(username)
    driver.find_element_by_id("LoginForm_password").click()
    driver.find_element_by_id("LoginForm_password").send_keys(password)
    driver.find_element_by_id("SubmitLoginBTN").click()