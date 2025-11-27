#功能测试
#1.写用例    TestCase
#2.执行用例   A.TestSuite存储用例  B.TestLoader 找用例，加载用例，存在testsuitel里面
#3.对比实际结果 期望结果 判定用例是否通过     #断言，assert
#4.出具测试报告  #TextRunner

import unittest
from online.unitest import math_mehod  #测试的目标类

#写一个测试类，对我们写的math mehod模块里面的类，进行单元测试
class TestMathMethod(unittest.TestCase):  #继承了unitest的Testcase类
    #编写测试用例
    #1.一个用例就是一个函数，不能传参，只有self关键字
    #2.所有的用例（所有的函数都是test开头 test_)
    def test_add_postive(self):
        res=math_mehod.MathMehod(1,1).add()
        print("1+1的结果是",res)
        #加一个断言:判断期望值与实际值的比对结果一致就算通过,不一致就算失败,assertEqual是TestCase类的函数
        try:
            self.assertNotEquals(-2,res,msg="两个数相加错误了")   #函数内部的调用,self.属性,msg是用例失败才会显示
        except AssertionError as e:
            print("出错了,断言错误是{0}".format(e))
            raise e   #异常处理完了之后记得要抛出去

    def test_add_zero(self):
        res=math_mehod.MathMehod(0,0).add()
        print("0+0的结果是",res)

    def test_add_negative(self):
        res=math_mehod.MathMehod(-1,-1).add()
        print("-1+-1的结果是",res)

class TestMulti(unittest.TestCase):  #继承了unitest的Testcase类
    #编写测试用例
    #1.一个用例就是一个函数，不能传参，只有self关键字
    #2.所有的用例（所有的函数都是test开头 test_)
    def test_multi_postive(self):
        res=math_mehod.MathMehod(1,1).multi()
        print("1x1的结果是",res)

    def test_multi_zero(self):
        res=math_mehod.MathMehod(0,0).multi()
        print("0x0的结果是",res)

    def test_multi_negative(self):
        res=math_mehod.MathMehod(-1,-1).multi()
        print("-1x-1的结果是",res)

if __name__=="__main__":
    unittest.main()     #执行所有的用例
