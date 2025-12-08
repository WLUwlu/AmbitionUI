# -*- coding: utf-8 -*-
import requests

class HttpRequest:
    """利用requests封装get请求和post请求"""

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

if __name__=="__main__":
    login_url="https://httpbin.org/post"
    data={"name":"123"}
    http=HttpRequest()
    res=http.http_request(login_url,data,"post")
    print("课堂派登录的结果是{0}".format(res))

