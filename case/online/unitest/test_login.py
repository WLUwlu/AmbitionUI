import unittest
from online.get_data import GetData
from online.http_request import HttpRequest

class TestHttp(unittest.Testcase):
    def setUp(self):
        #登录
        self.login_url="http://www.baidu.com"
        #充值的url
        self.recharge_url="http://www."

     def test_login_normal(self):  #正常登录
         data={"mobilephone":"1888888888","pwd":"123456"}
         res=HttpRequest().http_request(self.login_url,data,"get")
         if res.cookies:  #如果cookie有的话，那么就更新cookie
             setattr(GetData,"Cookie",re)
         try:
             self.assertEqual("10001",res.json()["code"])
         except AssertionError as e:
             print("test_login_normal error is{}".format(e))
             raise e

     def test_login_wrong_pwd(self):  #输入错误的密码
         data={"mobilephone":"1888888888","pwd":"123456789"}
         res=HttpRequest().http_request(self.login_url,data,"get")
         try:
             self.assertEqual("20111",res.json()["code"])
         except AssertionError as e
             print("test_login_wrong_pwds error is{}".format(e))
             raise e
         print(res.json())



     def test_recharge_normal(self):  #正常充值
         recharge_data={"mobilephone":"1888888888","amount":"1000"}
         res=HttpRequest().http_request(self.recharge_url,recharge_data,"post",getattr(GetData,"Cookie"))
         try:
             self.assertEqual("10001",res.json()["code"])
         except AssertionError as e:
             print("test_recharge_normal's error is{}".format(e))


     def test_charge_negative(self):  #充值为负数
         recharge_data = {"mobilephone": "1888888888", "amount": "-1000"}
         res = HttpRequest().http_request(self.recharge_url, recharge_data, "post", getattr(GetData, "Cookie"))
         try:
             self.assertEqual("10001", res.json()["code"])
         except AssertionError as e:
             print("test_recharge_normal's error is{}".format(e))
