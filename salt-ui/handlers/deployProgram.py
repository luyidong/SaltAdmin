#!/usr/bin/env python
#coding=utf-8
#__author__  = louis,
# __date__   = 2016-06-01 17:05,
#  __email__ = yidongsky@gmail.com,
#   __name__ = deployProgram.py

import tornado.web
import  re
import json

from saltapi import SaltAPI
import settings
import requests

class CreateProgramHandler(tornado.web.RequestHandler):
    def get(self):
        program   = self.get_argument("program")
        env       = self.get_argument("env")
        #nodegroup  = self.get_argument("nodegroup")
        soft       = self.get_argument("soft")
        if program and env and soft:
            header = {
                "content-type":"application/json"
            }
            try:
                url="http://10.11.100.248:9000/salt/prom?program=%s&env=%s" % (program,env)
                #url="http://localhost:9000/salt/prom?program=%s&env=%s" % (program,env)
                response = requests.post(url,headers=header,timeout=3)
                print response.json()
                r = response.json()
                print r['result']
                self.write(json.dumps(response.json()))

            except Exception,e:
                print Exception,":",e



class nodegroupHandler(tornado.web.RequestHandler):
    def get(self):
        program   = self.get_argument("program")
        env        = self.get_argument("env")
        #nodegroup  = self.get_argument("nodegroup")
        soft       = self.get_argument("soft")
        if program and env and soft:
            try:
                url="http://10.11.100.248:9000/salt?program=%s&env=%s" % (program,env)
                #url="http://localhost:9000/salt?program=%s&env=%s" % (program,env)
                response = requests.post(url,timeout=3)
                print response.json()
                r = response.json()
                print r['result']
                self.write(json.dumps(response.json()))

            except Exception,e:
                print Exception,":",e





    #     if env == ('beta'|'dev'):
    #         saltapi = SaltAPI(
    #             url=settings.SALT_API['url'],
    #             username=settings.SALT_API['user'],
    #             password=settings.SALT_API['password']
    #         )
    #     elif env == ('preview'|'online'):
    #         saltapi = SaltAPI(
    #             url=settings.SALT_API['url'],
    #             username=settings.SALT_API['user'],
    #             password=settings.SALT_API['password']
    #         )
    # def  checkProm:





# class groupHandler(tornado.web.RequestHandler):
# class hostlistHandler(tornado.web.RequestHandler):
# class pillarHandler(tornado.web.RequestHandler):

# class logstashHandler(tornado.web.RequestHandler):
# class zabbixHandler(tornado.web.RequestHandler):
# class rsyncHandler(tornado.web.RequestHandler):
