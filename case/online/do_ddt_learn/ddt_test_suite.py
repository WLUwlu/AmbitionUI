#coding=utf-8

import unittest


loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttp))

#执行
with open("test_summer.html","wb") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,verosity=2,title=None,description=)
    runner.run(suite)