import unittest
from web.case import math_mehod,danyuantest01

suite=unittest.TestSuite()   #存储用例的实例，一个存储测试用例的容器
#方法一：
#只执行一条，两个正数相加
suite.addTest(TestMathMehod("test_add_postive"))
suite.addTest(TestMathMehod("test_add_zero"))


#方法二：Testloader
loader=unittest.TestLoader()  #创建一个加载器
#suite.addTest(loader.loadTestsFromTestCase(TestMathMehod))        #从名字寻找用例，找到后用addtest方法加到容器中
from web.case import danyuantest01   #导入具体到模块
suite.addTest(loader.loadTestsFromModule(danyuantest01))                        #从模块寻找用例

runner=unittest.TextTestRunner()
runner.run(suite)