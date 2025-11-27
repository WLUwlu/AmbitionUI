import unittest
from online.unitest import math_mehod,danyuantest01
from danyuantest01 import TestMathMethod   #引用具体到类名


suite=unittest.TestSuite()   #存储用例的实例，一个存储测试用例的容器
#方法一：
#只执行一条，两个正数相加
suite.addTest(TestMathMethod("test_add_postive"))
suite.addTest(TestMathMethod("test_add_zero"))


#方法二：Testloader
loader=unittest.TestLoader()  #创建一个加载器
#suite.addTest(loader.loadTestsFromTestCase(MathMehod)        #从名字寻找用例，找到后用addtest方法加到容器中

#from online.unitest import danyuantest01  #导入具体到模块
#suite.addTest(loader.loadTestsFromModule(danyuantest01))                        #从模块寻找用例




with open("test.txt","w+",encoding="utf-8") as file:   ##w+:没有该文件会新建文件；w特点：文件指针在开头，用新内容覆盖原内容
    runner=unittest.TextTestRunner(stream=file, verbosity=0)
    runner.run(suite)
print(file.closed)


with open("test_report.html","wb") as file:
    runner=HTMLTest