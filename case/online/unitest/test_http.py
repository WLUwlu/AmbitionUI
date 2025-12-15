from case.unitest.get_data import GetData

class TestHttp(unittest.TestCase):
    def setup(self):#重写
        print("开始测试啦")

    def __init__(self,methodName,url,data,method,expected): #通过初始化参数来传参
        super(TestHttp,self).__init__(methodName)  #父类的方法保留了
        self.url=url
        self.data=data
        self.method=method
        self.excepted=expected

    #超继承
    def test_api(self):  #接口用例
        res=HttpRequest().http_request(self.url,self.data,self.method,getattr(GetData.Cookie))
        if res.cookies: #如果cookie有的话，就更新cookie
            setattr(GetData,"cookie")  #反射
        try:
            self.assertEqual(self.excepted,res.json()["code"])
        except AssertionError as e:
            print("test_api error is{}".format(e))
            raise e
        print(res.json())


