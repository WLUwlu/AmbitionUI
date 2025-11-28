# -*- coding: utf-8 -*-



import unittest

from online.tools.test_func import *

class TestFunc(unittest.TestCase):

  """Test test_func.py"""

  @classmethod
  def setUpClass(cls):
    print("This setUpClass() method only called once.")

  @classmethod
  def tearDownClass(cls):
    print("This tearDownClass() method only called once too.")





  @unittest.skip('test_add')   #跳过某个用例不执行

  def test_add(self):

    """Test func add"""

    self.assertEqual(3, add(1, 2))

    self.assertNotEqual(3, add(1, 3))

  def test_multi(self):

    """Test func multi"""

    self.assertEqual(6, multi(2, 3))

    self.assertNotEqual(8, multi(3, 3))

    self.skipTest('不想测test_multi')

  def test_lower_str(self):

    """Test func lower_str"""

    self.assertEqual("abc", lower_str("ABC"))

    self.assertNotEqual("Dce", lower_str("DCE"))

  def test_square(self):

    """Test func square"""

    self.assertEqual(17, square(4)) # 这里故意设计一个会出错的用例，测试4的平方等于17，实际上并不等于。

    self.assertNotEqual(35, square(6))


if __name__ == '__main__':
  unittest.main(verbosity=2)
