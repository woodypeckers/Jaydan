# -*- coding:utf-8 -*-
# author:Jaydan

import time
import appium

def open_url(driver,url):
    driver.get(url)


def capabilities():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '88AKBME2356N'
    # desired_caps['app'] = 'com.iqtogether.qxueyou.apk'  #获取pc端的apk，没有的话会自动安装
    desired_caps['appPackage'] = 'io.jjyang.joylite'
    desired_caps['appActivity'] = '.SplashActivity'
    desired_caps['noReset'] = 'true'