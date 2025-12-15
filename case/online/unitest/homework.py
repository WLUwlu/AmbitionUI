import requests
import unittest
from parameterized import parameterized,param
import HTMLTestRunner

class HttpRequestModo(unittest.TestCase):
    #测试类加上异常处理以及断言
    def http_request(self,url,data,method,cookie=None):
        """url请求的地址
        param:传递的参数,非必填参数,字典的格式传递参数
        method:请求方式 支持get以及post字符串形式的参数
        cookies:请求的时候传递的cookie值"""
        if method == "get":
            res=requests.get(url,cookies=cookie,verify=False)  #响应结果的消息实体
        else:
            res=requests.post(url,data,cookies=cookie,verify=False)  #响应结果的消息实体
        return res   #返回一个消息实体

class testCase(HttpRequestModo):

    def setUp(self):
        print("我要开始执行用例")


    def tearDown(self):
        print("我已经执行完用例了")

    @parameterized.expand([
        param("name",""),
        param("name","password"),
        param("","password"),
        param("name","pass")
    ])
    def test_loginApi(self):
        """正常登录，不输密码，不输账号，错误密码"""
        login_url="https://httpbin.org/post"
        http = HttpRequestModo()
        data={}
        res = http.http_request(login_url, data, "post")

    @parameterized.expand([
        param("name", "","20"),
        param("name", "password","20"),
        param("", "password","20"),
        param("name", "pass","-20")
    ])
    def test_rechargeApi(self):
        """正常充值，不输账号，不输金额，错误金额负数"""
        kq_url= "https://httpbin.org/get"
        http = HttpRequestModo()
        data = {}
        res = http.http_request(kq_url, data, "post")



#生成html类型的测试报告
# 使用discover()来实现添加执行整个目录下所有的测试用例
import os
import unittest
import HTMLTestRunner
import time






if __name__ == '__main__':
    # 获取用例目录
    case_dir = os.path.join(os.path.dirname(__file__), 'all_case')

    # 创建测试套件
    suite = unittest.TestSuite()

    # 使用不同的加载方法
    loader = unittest.TestLoader()

    # 方法1：加载目录中的所有测试
    suite = loader.discover(case_dir, pattern='test*.py')

    # 或者方法2：如果知道具体的测试类
    # from all_case.test_example import TestExample
    # suite.addTest(loader.loadTestsFromTestCase(TestExample))

    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # 加个时间戳
    now = time.strftime("%y-%m_%d_%H_%M_%S_",time.localtime(time.time()))

    # 创建html类型测试报告对象，将执行的过程写入到file_obj中
    file_obj = open("D:/pythonProject/P7_P8_Requests/"
                    "unittest框架/test_report/"
                    "{}test_report.html".format(now),"w+",encoding="utf-8")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    report_dir = os.path.join(current_dir, "test_report")
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # 创建配置html测试报告的相关信息的对象
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_obj,
                                           title="第一次的测试报告",
                                           description="我是测试报告的描述信息")
    # 生成html测试报告；如果要生成测试报告，则不通过unittest.main()方法执行
    runner.run(suite)
