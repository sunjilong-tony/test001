#! /usr/bin/python3
# coding= utf-8
import unittest
import time
from HTMLTestRunner import HTMLTestRunner


suite = unittest.defaultTestLoader.discover("e:/python2/测试/main", pattern="test*.py")
file_path = "e:/python2/测试/report/{}.html".format(time.strftime("%y-%m-%d %H-%M-%S"))
with open(file_path, "wb") as f:
    HTMLTestRunner(stream=f, title="测试报告").run(suite)
