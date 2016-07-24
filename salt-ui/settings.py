#!/usr/bin/env python
#coding=utf-8
#__author__  = louis,
# __date__   = 2016-04-20 01:11,
#  __email__ = yidongsky@gmail.com,
#   __name__ = settings.py

import os.path
#模板路径
Template_Path = os.path.join(os.path.dirname(__file__),"templates")
#静态文件路径
Static_Path = os.path.join(os.path.dirname(__file__),"static")
#设置cookie
Cookie_Secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E="
#登陆路径
Login_Url="/auth/login"
AUTOESCAPE = None
#开启调试模式
Debug = True
#防范请求伪造
Xsrf_Cookies = False


# salt-api setting
SALT_API = {
    'url': 'https://10.202.184.248:8000',
    #'url': 'https://172.24.30.11:8000',
    'user': 'saltadmin',
    'password': 'p@ssw0rd'
}