#!/usr/bin/env python
#coding=utf-8
#__author__  = 'louis',
# __date__   = '2016-04-20 01:14',
#  __email__ = 'yidongsky@gmail.com',
#   __name__ = 'main.py'

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import settings as setting_coustom
import urls
import dbutil.torndb as torndb

#import torndb

#支持中文编码
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_database", default="OPserver", help="blog database name")
define("mysql_user", default="root", help="blog database user")
define("mysql_password", default="", help="blog database password")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls.handlers
        #配置字典
        settings = dict(
            #模板路径
            template_path = setting_coustom.Template_Path,
            #静态文件路径
            static_path = setting_coustom.Static_Path,
            #设置cookie
            cookie_secret=setting_coustom.Cookie_Secret,
            #登陆路径
            login_url=setting_coustom.Login_Url,
            #开启调试模式
            debug = setting_coustom.Debug,
            #UI模块
            #ui_modules = urls.uiModules,
            #防范请求伪造
            xsrf_cookies = setting_coustom.Xsrf_Cookies,
        )
        #在初始化子类的调用中路由列表和配置字典的值
        tornado.web.Application.__init__(self,handlers,**settings)

        # Have one global connection to the blog DB across all handlers
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password,
            max_idle_time=25200, connect_timeout=10, time_zone='+08:00', charset='utf8',
            sql_mode='TRADITIONAL')


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()