#!/usr/bin/env python
#coding=utf-8
#__author__  = louis,
# __date__   = 2016-04-20 01:13,
#  __email__ = yidongsky@gmail.com,
#   __name__ = urls.py

import tornado.web as web

from handlers.base import HelloModule,AllkeysHandler,UnacceptkeysHandler,DeniedkeysHandler,RejectedkeysHandler,BaseHandler,deleteMinionKeysHandler,acceptMinionKeysHandler,deleteRejectKeysHandler,deletedeniedKeysHandler
from handlers.deployProgram import CreateProgramHandler,nodegroupHandler
from handlers.auth import  Mainhandler,AuthCreateHandler,AuthLoginHandler,AuthLogoutHandler
from handlers.user import UserlistHandler,UserHandler,RolelistHandler,RoleHandler,PermissionHandler,PermissionlistHandler

#首页
from handlers.base import indexDevops
#CMDB
from handlers.cmdb import indexCMDB,listCMDB,listHandler,delCMDBHandler,submitCMDBHandler,updateCMDBHandler,addListHandler,addHandler,ChartHandler,Promlist,indexProm,indexEnv,Envlist


handlers = [
   #路由列表
   #CMDB
   (r"/",indexDevops),
   (r"/cmdb",indexCMDB),
   (r"/cmdb/list",listCMDB),
   (r"/cmdb/listTable",listHandler),
   (r"/cmdb/delTable",delCMDBHandler),
   (r"/cmdb/updatelist",updateCMDBHandler),
   (r"/cmdb/update",submitCMDBHandler),
   (r"/cmdb/addlist",addListHandler),
   (r"/cmdb/add",addHandler),
   (r"/cmdb/chart",ChartHandler),
   (r"/cmdb/promlist",Promlist),
   (r"/cmdb/prom",indexProm),
   (r"/cmdb/env",indexEnv),
   (r"/cmdb/envlist",Envlist),

   (r"/hello",HelloModule),
   (r"/v1",Mainhandler),
   (r"/auth/create", AuthCreateHandler),
   (r"/auth/login", AuthLoginHandler),
   (r"/auth/logout", AuthLogoutHandler),
   (r"/user",UserHandler),
   (r"/role/",RoleHandler),
   (r"/user/list",UserlistHandler),
   (r"/role/list",RolelistHandler),
   (r"/permission/",PermissionHandler),
   (r"/permission/list",PermissionlistHandler),

   (r"/salt",BaseHandler),
   (r"/salt/allkeys",AllkeysHandler),
   (r"/salt/unacceptkeys",UnacceptkeysHandler),
   (r"/salt/deniedkeys",DeniedkeysHandler),
   (r"/salt/rejectedkeys",RejectedkeysHandler),
   (r"/salt/deleteMinionKeys",deleteMinionKeysHandler),
   (r"/salt/acceptMinionKeys",acceptMinionKeysHandler),
   (r"/salt/deleteRejectKeys",deleteRejectKeysHandler),
   (r"/salt/deletedeniedkeys",deletedeniedKeysHandler),

   (r"/salt/api/prom",CreateProgramHandler),
   (r"/salt/api/nodegroup",nodegroupHandler),
   (r"/images/(.*)", web.StaticFileHandler,{"path":"/Users/louis/PycharmProjects/OPserver/static/datatable/images"}),
   (r"/static/(.*)", web.StaticFileHandler,{"path":"/Users/louis/PycharmProjects/OPserver/static"}),
]
#uiModules = {'Hello': HelloModule}


