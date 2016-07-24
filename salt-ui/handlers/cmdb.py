#!/usr/bin/env python
#coding=utf-8
#__author__  = louis,
# __date__   = 2016-07-11 14:44,
#  __email__ = yidongsky@gmail.com,
#   __name__ = cmdb.py

import tornado.web
import json,time
from cmdb_table import listCmdbTable,listPromTable,listEnvTable

from datetime import date, datetime
#支持中文编码
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def default(slef,obj):
        # 解决Json中存在datetime类型数据
        """JSON serializer for objects not serializable by default json code"""
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

class indexCMDB(BaseHandler):
    def get(self):
        self.render("cmdb/index.html")

class listCMDB(BaseHandler):
    def get(self):
        self.render("cmdb/list.html")

class indexProm(BaseHandler):
    def get(self):
        self.render("cmdb/prom.html")

class indexEnv(BaseHandler):
    def get(self):
        self.render("cmdb/env.html")


class listHandler(BaseHandler):
    def get(self):
        sEcho = self.get_argument("sEcho")
        sSortDir = self.get_argument("sSortDir_0")
        sortCol = self.get_argument("iSortCol_0")
        displayStart = self.get_argument("iDisplayStart")
        search = self.get_argument("sSearch")
        sortingCol = self.get_argument("iSortingCols")
        displayLength = self.get_argument("iDisplayLength")
        data = listCmdbTable()
        data.setDataTableOptions( sEcho,sSortDir,sortCol,displayStart,search,sortingCol,displayLength) #echo sortdir sortcol displaystart search sortingcolumns displaylength
        self.write(data.getDataTableData())

class Promlist(BaseHandler):
    def get(self):
        sEcho = self.get_argument("sEcho")
        sSortDir = self.get_argument("sSortDir_0")
        sortCol = self.get_argument("iSortCol_0")
        displayStart = self.get_argument("iDisplayStart")
        search = self.get_argument("sSearch")
        sortingCol = self.get_argument("iSortingCols")
        displayLength = self.get_argument("iDisplayLength")
        data = listPromTable()
        data.setDataTableOptions( sEcho,sSortDir,sortCol,displayStart,search,sortingCol,displayLength) #echo sortdir sortcol displaystart search sortingcolumns displaylength
        self.write(data.getDataTableData())

class Envlist(BaseHandler):
    def get(self):
        sEcho = self.get_argument("sEcho")
        sSortDir = self.get_argument("sSortDir_0")
        sortCol = self.get_argument("iSortCol_0")
        displayStart = self.get_argument("iDisplayStart")
        search = self.get_argument("sSearch")
        sortingCol = self.get_argument("iSortingCols")
        displayLength = self.get_argument("iDisplayLength")
        data = listEnvTable()
        data.setDataTableOptions( sEcho,sSortDir,sortCol,displayStart,search,sortingCol,displayLength) #echo sortdir sortcol displaystart search sortingcolumns displaylength
        self.write(data.getDataTableData())


class delCMDBHandler(BaseHandler):
    def get(self):
        id = self.get_argument("server_ip",None)
        print id
        ids = id.split(',')
        if id:
            for row in ids:
                print 'row:',row
                sql = self.db.execute("delete from server_list where server_ip = %s",row)
                print sql
                self.write(json.dumps(sql))

    def post(self):
        id = self.get_argument("server_ip",None)
        ids = id.split(',')
        if id:
            for row in ids:
                print 'row:',row
                sql = self.db.execute("delete from server_list where server_ip =  %s",row)
                print sql
                res = {'result':'ok'}
                self.write(json.dumps(res))

class updateCMDBHandler(BaseHandler):
    def get(self):
        server_stat = self.db.query("SELECT * FROM OPserver.server_status_categ")
        server_fun = self.db.query("SELECT id,fun_categ_name FROM OPserver.server_fun_categ")
        server_env = self.db.query("SELECT id,env_categ_name FROM OPserver.server_env_categ")
        serverIp = self.get_argument("serverip",None)
        if serverIp:
            server_attr = self.db.get("SELECT * FROM OPserver.server_list where server_ip=%s",(serverIp))
            #print 'ids %s',serverIp
            #print 'sas,%s',sa_list
            print 'serverip,%s',server_attr
            # res = {"serverIP":serverips,"sa_list":sa_list }
            res = {"server_attr":server_attr,"server_env":server_env,"server_fun":server_fun,"server_stat":server_stat}
            self.write(json.dumps(res,default=self.default))


class submitCMDBHandler(BaseHandler):
    def post(self):
        action_type = self.get_argument("action_type")
        serverip = self.get_argument("serverip",None)
        sname = self.get_argument("servername",None)
        prom= self.get_argument("prom",None)
        env = self.get_argument("env",None)
        status = self.get_argument("status",None)

        t=int(time.time())
        last_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))

        if action_type and serverip:
            sql = 'update %s set server_name="%s",server_ip="%s",server_status_id="%s",server_fun_id="%s",server_env_id="%s",server_last_time="%s" where server_ip="%s"' %(action_type,sname,serverip,status,prom,env,last_time,serverip)
            res = self.db.execute(sql)
            self.write(json.dumps(res))


class addListHandler(BaseHandler):
    def get(self):
        server_stat = self.db.query("SELECT * FROM OPserver.server_status_categ")
        server_fun = self.db.query("SELECT id,fun_categ_name FROM OPserver.server_fun_categ")
        server_env = self.db.query("SELECT id,env_categ_name FROM OPserver.server_env_categ")
        server_attr = {"server_env_id": 1,"server_status_id": "1", "server_fun_id": 1}
        res = {"server_attr":server_attr,"server_env":server_env,"server_fun":server_fun,"server_stat":server_stat}
        self.write(json.dumps(res,default=self.default))


class addHandler(BaseHandler):
    def post(self):
        action_type = self.get_argument("action_type")
        serverip = self.get_argument("serverip",None)
        sname = self.get_argument("servername",None)
        prom= self.get_argument("prom",None)
        env = self.get_argument("env",None)
        status = self.get_argument("status",None)

        t=int(time.time())
        last_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))

        server_ip = self.db.query("select server_ip from server_list")
        server_stat = self.db.query("SELECT * FROM OPserver.server_status_categ")
        server_fun = self.db.query("SELECT id,fun_categ_name FROM OPserver.server_fun_categ")
        server_env = self.db.query("SELECT id,env_categ_name FROM OPserver.server_env_categ")
        server_attr = {"server_env_id": 1,"server_status_id": "1", "server_fun_id": 1}

        #res = {"server_attr":server_attr,"server_env":server_env,"server_fun":server_fun,"server_stat":server_stat}
        #self.write(json.dumps(res,default=self.default))
        #print serverip
        count = 0
        for m in range(len(server_ip)):
            #print  server_ip[m]

            for k,v in server_ip[m].items():
                print 'item:' ,k,v


                if v == serverip:
                    print v
                    count += 1
                    break
                else:
                    count = 0

                print count

                if count != 1 :

                    res = self.db.execute("INSERT INTO %s ( server_name,server_ip,server_status_id,server_fun_id,server_env_id,server_last_time) VALUES ('%s','%s','%s','%s','%s','%s') ON DUPLICATE KEY UPDATE server_ip='%s'" %(action_type,str(sname),str(serverip),str(status),str(prom),str(env),str(last_time),str(serverip)))
                    obj = "ok"
                    #print obj

                    self.write(json.dumps(0))
                else:

                    mes = 'ip err'
                    print mes
                    # res = 'err'
                    obj = {"data":'err'}
                    print obj
                    self.write(json.dumps(obj))



class ChartHandler(BaseHandler):
    def get(self):
        sql = 'select s.server_name,f.fun_categ_name as prom from ((server_list as s inner join server_env_categ  as c on s.server_env_id=c.id ) inner join  server_fun_categ as f on s.server_fun_id=f.id) inner join server_status_categ as n on s.server_status_id = n.id '
        obj = {
            'title':[],
            'data':[]
        }
        res = {}
        for c in self.db.query(sql):
            age = c.values()[0]

            res[age] = res.get(age,0)+1
        print res.items()
        for age,num in res.items():
            print age,num
            obj['title'].append('%s 应用'%(age))
            obj['data'].append({
                'name':'%s'%(age),
                'value':num
            })
        self.write(json.dumps(obj))
