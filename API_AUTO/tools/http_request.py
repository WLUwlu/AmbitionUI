import requests

class HttpRequest:
    """利用request封装get"请求和post请求
    url:请求的地址"
    param:传递的参数 非必填参数，字典的格式传递参数"
    method:请求方式get，以及post,字符串形式的参数
    cookie：请求的时候传递的cookie值
    """
    def http_request(self,url,data,method,cookie=None):
        if method.lower=="get":
            res = requests.get(url, data, cookies=cookie)  # 返回一个消息实体（状态码）
        else:
            res = requests.post(url,data,cookies=cookie)  # 返回一个消息实体（状态码）
        return res  #返回一个消息实体

if __name__=="__main__":
    url = "https://ptlogin.3304399.net/resource/images/spriteV2.png?v=131127"
    data = {"mobile": "1065092736@11.com"}
    res=HttpRequest().http_request(url,data,"get")
    print("登录结果是：",res.json)


    recharge_url="https://ptlogin.3304399.net/resource/images/q_sprite.png?v=130504"
    recharge_data={"mobiephone":"15826558950"}
    recharge_res=HttpRequest().http_request(recharge_url,recharge_data,"post")
    print("充值结果是：",recharge_res.json)

