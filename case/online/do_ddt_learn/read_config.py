#coding=utf-8

import configparser

class ToolsConfig:
    def read_config(self,file_name,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_name,encoding="utf-8")
        return cf.get(section,option)

if __name__=="__main__":
    res=ToolsConfig().read_config("tools.config","MODE","mode")
    print(res)

