import unittest

from  online.unitest.our_testcase import TestFunc

if __name__ == '__main__':

  suite = unittest.TestSuite()

  tests = [TestFunc("test_square"), TestFunc("test_lower_str"), TestFunc("test_multi")]

  suite.addTests(tests)

  runner = unittest.TextTestRunner(verbosity=2)

  runner.run(suite)

# 直接用addTest方法添加单个TestCase

  suite.addTest(TestMathFunc("test_multi"))

  # 使用loadTestFromName,传入模块名.TestCase名，下面俩方法效果相同

  suite.addTests(unittest.TestLoader().loadTestsFromName('our_testcase.TestFunc'))

  suite.addTests(unittest.TestLoader().loadTestsFromNames(['our_testcase.TestFunc']))

  # loadTestsFromTestCase()，传入TestCase

  suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFunc))
