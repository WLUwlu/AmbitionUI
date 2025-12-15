#coding=utf-8


#ddt +unittest来进行数据的处理，第三方库
#装饰器，会在函数运行之前运行
import unittest
from ddt import ddt,data,unpack

#test_data=[[1,3,7],[4,5,8]] #[1,3,7],[4,5,8]两个数据

test_data=[{"no":1,"name":"文档"},{"no":2,"name":"温度"}]

@ddt   #装饰测试类
class TestMath(unittest.TestCase):

    @data(*test_data)
    @unpack
    def test_print_data(self,a,b):  # 参数名必须与字典的键匹配
        print("no",no)
        print("name",name)





    # def test_add(self):
    #     a=10
    #     b=20
    #     print(a+b)

