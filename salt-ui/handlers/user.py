#!/usr/bin/env python
#coding=utf-8
#__author__  = louis,
# __date__   = 2016-05-03 17:07,
#  __email__ = yidongsky@gmail.com,
#   __name__ = uesr.py

#支持中文编码
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import tornado.web
import torndb
from json import dumps
import MySQLdb as mysql
#from table import Table
import time
import json
from datetime import date, datetime

from table import UserlistTable,RolelistTable,PermisslistTable

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def date_handler(obj):
        return obj.isoformat() if hasattr(obj, 'isoformat') else obj

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

class UserHandler(BaseHandler):
    def get(self):
        userlist = self.db.query("select u.userid,u.username,u.nickname,u.email,s.userstat,r.name as role,u.last_login from user as u inner join role  as r on (r.roleid=u.role_id) inner join user_stat s on (u.is_active=s.statid)")
        print userlist
        #self.write(dumps(userlist,cls=DatetimeEncoder))
        self.render("user.html")

class RoleHandler(BaseHandler):
    def get(self):
        rolelist = self.db.query("SELECT * FROM fable.role")
        print rolelist
        #self.write(dumps(rolelist,cls=DatetimeEncoder))
        self.render("role.html")

class PermissionHandler(BaseHandler):
    def get(self):
        permisslist = self.db.query("SELECT * FROM fable.user_permission")
        print permisslist
        #self.write(dumps(permisslist,cls=DatetimeEncoder))
        self.render("permission.html")


class UserlistHandler(tornado.web.RequestHandler):
    def get(self):
        sEcho = self.get_argument("sEcho")
        sSortDir = self.get_argument("sSortDir_0")
        sortCol = self.get_argument("iSortCol_0")
        displayStart = self.get_argument("iDisplayStart")
        search = self.get_argument("sSearch")
        sortingCol = self.get_argument("iSortingCols")
        displayLength = self.get_argument("iDisplayLength")
        data = UserlistTable()
        data.setDataTableOptions( sEcho,sSortDir,sortCol,displayStart,search,sortingCol,displayLength) #echo sortdir sortcol displaystart search sortingcolumns displaylength
        #return data.getDataTableData()
        self.write(data.getDataTableData())

class RolelistHandler(tornado.web.RequestHandler):
    def get(self):
        sEcho = self.get_argument("sEcho")
        sSortDir = self.get_argument("sSortDir_0")
        sortCol = self.get_argument("iSortCol_0")
        displayStart = self.get_argument("iDisplayStart")
        search = self.get_argument("sSearch")
        sortingCol = self.get_argument("iSortingCols")
        displayLength = self.get_argument("iDisplayLength")
        data = RolelistTable()
        data.setDataTableOptions( sEcho,sSortDir,sortCol,displayStart,search,sortingCol,displayLength) #echo sortdir sortcol displaystart search sortingcolumns displaylength
        #return data.getDataTableData()
        self.write(data.getDataTableData())

class PermissionlistHandler(tornado.web.RequestHandler):
    def get(self):
        sEcho = self.get_argument("sEcho")
        sSortDir = self.get_argument("sSortDir_0")
        sortCol = self.get_argument("iSortCol_0")
        displayStart = self.get_argument("iDisplayStart")
        search = self.get_argument("sSearch")
        sortingCol = self.get_argument("iSortingCols")
        displayLength = self.get_argument("iDisplayLength")
        data = PermisslistTable()
        data.setDataTableOptions( sEcho,sSortDir,sortCol,displayStart,search,sortingCol,displayLength) #echo sortdir sortcol displaystart search sortingcolumns displaylength
        #return data.getDataTableData()
        self.write(data.getDataTableData())

