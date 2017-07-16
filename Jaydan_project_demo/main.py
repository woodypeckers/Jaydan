# -*- coding:utf-8 -*-
# author:Jaydan

import time
import unittest
from HTMLTestRunner import HTMLTestRunner

def suites():
    suite = unittest.Testsuite()
    loader = unittest.Testloader()
    suite.addTest(loader.loadTestsFromTestCase())

if __name__ == "__main__":
    suite = suites()
    fp = open('./reports/results_%s.html'% time.strftime("%y-%m-%d %H-%M-%S"),'wb')
    runner = HTMLTestRunner(stream = fp,title = u'Bugfree_test_result',description = u'测试用例的情况：')
    runner.run(suite)