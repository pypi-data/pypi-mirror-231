#!/Users/christmas/opt/anaconda3/bin/python3
# -*- coding: utf-8 -*-
#  日期 : 2023/7/20 19:45
#  作者 : Christmas
#  邮箱 : 273519355@qq.com
#  项目 : Project
#  版本 : python 3
#  摘要 :
"""
    用于存放参数的类
"""


class P_para:
    def __init__(self, dict=False, **kwargs):
        if not dict:
            self.__dict__.update(kwargs)
        else:
            self.__dict__ = dict
    
    def __repr__(self):
        # return str(self.__dict__)
        return str(self.__class__.__name__)
    
    def addParam(self, **kwargs):
        self.__dict__.update(kwargs)
    
    def getParam(self, key):
        return self.__dict__[key]
    
    def getParams(self):
        return self.__dict__
    
    def delParam(self, key):
        del self.__dict__[key]
