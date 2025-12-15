#coding=utf-8

import unittest
import HTMLTestRunner
from online.tools.test_http import TestHttp  #类名
form online.tools.do_excel_2 import DoExcel

t=DoExcel("xh.xlsx","Python")

suite=unittest.TestSuite()
for i in range(1,t.max_row+1): #创建实例
    suite.addTest(TestHttp("test_api",t.get_data(i,j),))
#实例化的方式去加载用例url,data，method,excepted

#执行
with open("test_summer.html","wb") as file:
    runner=HTMLTestRunner.HTMLTestRunner(stream=file,verbosity= 2,title=)
