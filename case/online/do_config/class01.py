#配置文件
#properties  config ini log4j

#python中的configparser类 ，可以读取配置信息

import configparser

#section option value  key：value

cf=configparser.ConfigParser()
cf.read("case.config",encoding="utf-8")

#读取配置文件的数据
res_1=cf.get("MODE","mode")
print(res_1)

res_2=cf["MODE"]["mode"]
print(res_2)
