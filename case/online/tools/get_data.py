class GetData:
    Cookie=None  #存储cookie，初始值为None

if __name__=="__main__":
    print(GetData.Cookie)
    setattr(GetData,"Cookie","小黄")  #设置他的属性,可以直接把类里面的属性值做修改，把cookie的值改成小黄
    print(hasattr(GetData,"Cookie"))  #判断里面有没有这个属性值
    print(getattr(GetData,"Cookie"))  #获取这个类里面cookie的值，attrbute属性
    delattr(GetData,"Cookie")         #删除这个属性
    print(hasattr(GetData,"Cookie"))  #判断里面有没有这个属性值


