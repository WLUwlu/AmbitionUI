import requests

#get请求
url="http://test.xmodo.cn/mods/22946-1303"
res=requests.get(url)  #返回一个消息实体（状态码）
print(res)

#响应头 响应状态码 响应报文
print("响应头",res.headers)
print("响应状态码：",res.text)