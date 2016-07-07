#!/usr/bin/env python
#coding=utf-8
#__author__  = louis,
# __date__   = 2016-06-06 17:16,
#  __email__ = yidongsky@gmail.com,
#   __name__ = saltapiUtils.py

import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
import commands
import logging


from tornado.options import define, options
define("port", default=9000, help="run on the given port", type=int)

settings = {
    "debug": True,
}

from saltapiUtils import api

class testPingHandler(tornado.web.RequestHandler):
    def post(self):
        node = self.get_argument("node")
        res = api(node=node)
        result={}
        if res.testPing():
            result['result'] = True
            result['messages'] = 'test.ping ok'
            result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/testping?node=testprom01.beta1.fn'
            print result
            self.write(json.dumps(result))
        else:
            result['result'] = False
            result['messages'] = 'test.ping fail'
            result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/testping?node=testprom01.beta1.fn'
            print result
            self.write(json.dumps(result))

class AddNodeStateHandler(tornado.web.RequestHandler):
    def get(self):
        prom = self.get_argument("program")
        env = self.get_argument("env")
        node = self.get_argument("node")
        soft = self.get_argument("soft")
        result={}
        group = prom+'_'+env
        resCK = api(group=group)
        if resCK.checkGroup():
                if soft == 'php':
                    parg = 'webserver.'+prom+'.'+prom
                    res = api(node=node,arg=parg)
                    jid = res.AddNodeState()
                    result['id'] = node
                    result['jid'] = jid
                    result['result'] = True
                    result['messages'] = 'State PHP OK '
                    result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createstate?program=testprom&env=beta&node=testprom01.beta1.fn&soft=php'
                    print result
                    self.write(json.dumps(result))
                elif soft == 'java':
                    targ = 'webserver.'+prom+'.'+prom
                    res = api(node=node,arg=targ)
                    jid = res.AddNodeState()
                    result['id'] = node
                    result['jid'] = jid
                    result['result'] = True
                    result['messages'] = 'State Java OK'
                    result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/addnodestate?program=testprom&env=beta&node=testprom01.beta1.fn&soft=java'
                    print result
                    self.write(json.dumps(result))
                elif soft == 'logstash':
                    larg = 'base.nlogstash'
                    res = api(node=node,arg=larg)
                    jid = res.AddNodeState()
                    result['id'] = node
                    result['jid'] = jid
                    result['result'] = True
                    result['messages'] = 'State logstash OK'
                    result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createstate?program=testprom&env=beta&node=testprom01.beta1.fn&soft=logstash'
                    print result
                    self.write(json.dumps(result))
                elif soft == 'zabbix':
                    zarg = 'zabbix'
                    res = api(node=node,arg=zarg)
                    jid = res.AddNodeState()
                    result['id'] = node
                    result['jid'] = jid
                    result['result'] = True
                    result['messages'] = 'State Zabbix OK'
                    result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createstate?program=testprom&env=beta&node=testprom01.beta1.fn&soft=zabbix'
                    print result
                    self.write(json.dumps(result))
                elif soft == 'rundeck':
                    rarg = 'system.rundeck'
                    res = api(node=node,arg=rarg)
                    jid = res.AddNodeState()
                    result['jid'] = jid
                    result['result'] = True
                    result['messages'] = 'State Rundeck OK'
                    result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createstate?program=testprom&env=beta&node=testprom01.beta1.fn&soft=rundeck'
                    print result
                    self.write(json.dumps(result))
                else:
                    result['result'] = False
                    result['messages'] = 'State Error'
                    result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createstate?program=testprom&env=beta&node=testprom01.beta1.fn&soft=None'
                    print result
                    self.write(json.dumps(result))
        else:
            result['result'] = False
            result['messages'] = 'Error,Please check group'
            print result
            self.write(json.dumps(result))

class runStateHandler(tornado.web.RequestHandler):
    def get(self):
        prom = self.get_argument("program")
        env = self.get_argument("env")
        node = self.get_argument("node")
        soft = self.get_argument("soft")
        result={}
        group = prom+'_'+env
        resCK = api(group=group)
        if resCK.checkGroup():
                if soft == 'php':
                    parg = 'webserver.'+prom+'.'+prom
                    res = api(group=group,arg=parg)
                    jid = res.runState()
                    result['id'] = node
                    result['jid'] = jid
                    result['result'] = True
                    result['messages'] = 'State PHP OK '
                    result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createstate?program=testprom&env=beta&node=testprom01.beta1.fn&soft=php'
                    print result
                    self.write(json.dumps(result))
                elif soft == 'java':
                    targ = 'webserver.'+prom+'.'+prom
                    res = api(group=group,arg=targ)
                    jid = res.runState()
                    result['id'] = node
                    result['jid'] = jid
                    result['result'] = True
                    result['messages'] = 'State Java OK'
                    result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createstate?program=testprom&env=beta&node=testprom01.beta1.fn&soft=java'
                    print result
                    self.write(json.dumps(result))
                elif soft == 'logstash':
                    larg = 'base.nlogstash'
                    res = api(group=group,arg=larg)
                    jid = res.runState()
                    result['id'] = node
                    result['jid'] = jid
                    result['result'] = True
                    result['messages'] = 'State logstash OK'
                    result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createstate?program=testprom&env=beta&node=testprom01.beta1.fn&soft=logstash'
                    print result
                    self.write(json.dumps(result))
                elif soft == 'zabbix':
                    zarg = 'zabbix'
                    res = api(group=group,arg=zarg)
                    jid = res.runState()
                    result['id'] = node
                    result['jid'] = jid
                    result['result'] = True
                    result['messages'] = 'State Zabbix OK'
                    result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createstate?program=testprom&env=beta&node=testprom01.beta1.fn&soft=zabbix'
                    print result
                    self.write(json.dumps(result))
                elif soft == 'rundeck':
                    rarg = 'system.rundeck'
                    res = api(group=group,arg=rarg)
                    jid = res.runState()
                    result['jid'] = jid
                    result['result'] = True
                    result['messages'] = 'State Rundeck OK'
                    result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createstate?program=testprom&env=beta&node=testprom01.beta1.fn&soft=rundeck'
                    print result
                    self.write(json.dumps(result))
                else:
                    result['result'] = False
                    result['messages'] = 'State Error'
                    result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createstate?program=testprom&env=beta&node=testprom01.beta1.fn&soft=None'
                    print result
                    self.write(json.dumps(result))
        else:
            result['result'] = False
            result['messages'] = 'Error,Please check group'
            print result
            self.write(json.dumps(result))

class checkPHPHandler(tornado.web.RequestHandler):
    def get(self):
        prom = self.get_argument("program")
        env = self.get_argument("env")
        node = self.get_argument("node")
        soft = self.get_argument("soft")
        result={}
        group = prom+'_'+env
        check = api.checkPHP(group,node)
        if check and soft == 'php' :
            result['id'] = node
            result['result'] = True
            result['messages'] = 'Success, PHP init'
            result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/checkphp?program=testprom&env=beta&node=testprom01.beta1.fn&soft=php'
            print result
            self.write(json.dumps(result))
        else:
            result['result'] = False
            result['messages'] = 'Error,Please check %s ' % group
            print result
            self.write(json.dumps(result))

class checkLogstashHandler(tornado.web.RequestHandler):
    def get(self):
        prom = self.get_argument("program")
        env = self.get_argument("env")
        node = self.get_argument("node")
        soft = self.get_argument("soft")
        result={}
        group = prom+'_'+env
        checkLog = api.checkLogstash(group,node)
        if checkLog and soft == 'logstash' :
            result['id'] = node
            result['result'] = True
            result['messages'] = 'Success, Logstash init'
            result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/checklogstash?program=testprom&env=beta&node=testprom01.beta1.fn&soft=logstash'
            print result
            self.write(json.dumps(result))
        else:
            result['result'] = False
            result['messages'] = 'Error,Please check %s ' % group
            print result
            self.write(json.dumps(result))


class checkZabbixHandler(tornado.web.RequestHandler):
    def get(self):
        prom = self.get_argument("program")
        env = self.get_argument("env")
        node = self.get_argument("node")
        soft = self.get_argument("soft")
        result={}
        group = prom+'_'+env
        checkZab = api.checkZabbix(group,node)
        if checkZab and soft == 'zabbix' :
            result['id'] = node
            result['result'] = True
            result['messages'] = 'Success, Zabbix init'
            result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/checkzabbix?program=testprom&env=beta&node=testprom01.beta1.fn&soft=zabbix'
            print result
            self.write(json.dumps(result))
        else:
            result['result'] = False
            result['messages'] = 'Error,Please check %s ' % group
            print result
            self.write(json.dumps(result))

class createRundeckHandler(tornado.web.RequestHandler):
    def get(self):
        prom = self.get_argument("program")
        env = self.get_argument("env")
        node = self.get_argument("node")
        soft = self.get_argument("soft")
        result={}
        res = api(group=prom,env=env)
        if res.createRundeck():
            result['result'] = True
            result['messages'] = 'Success, Rundeck init'
            result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createrundeck?program=testprom&env=beta&node=testprom01.beta1.fn&soft=rundeck'
            print result
            self.write(json.dumps(result))
        else:
            result['result'] = False
            result['messages'] = 'Error,Please check %s ' % group
            print result
            self.write(json.dumps(result))

class checkPillarHandler(tornado.web.RequestHandler):
    def get(self):
        prom = self.get_argument("program")
        env = self.get_argument("env")
        node = self.get_argument("node")
        result={}
        group = prom+'_'+env
        #print 'group_item',group_item
        #group = '  '+prom+'_'+env
        res = api(group=group,node=node)
        node_item = node.split(',')
        for item in node_item:
            pillar_item= res.checkPillar()
           
            if  pillar_item:
                result['id'] = item
                result['result'] = True
                result['messages'] = 'Success,Refresh Pillar OK'
                result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/checkpillar?program=testprom&env=beta&node=testprom01.beta1.fn'
                print result
                self.write(json.dumps(result))
            else:
                result['id'] = item
                result['result'] = False
                result['messages'] = 'Error,Refresh Pillar Fail'
                result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/checkpillar?program=testprom&env=beta&node=testprom01.beta1.fn'
                print result
                self.write(json.dumps(result))

class checkNodeHandler(tornado.web.RequestHandler):
    def get(self):
        prom = self.get_argument("program")
        env = self.get_argument("env")
        node = self.get_argument("node")
        result={}
        group = '  '+prom+'_'+env
        res = api(group=group,node=node)
        node_item = node.split(',')
        for item in node_item:
            #group_item = res.checkNode()
            group_item = res.checkAlive()
           
            if  group_item:
                result['id'] = item
                result['result'] = True
                result['messages'] = 'Success,node is ok'
                result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/checknode?program=testprom&env=beta&node=testprom01.beta1.fn'
                print result
                self.write(json.dumps(result))
            else:
                result['id'] = item
                result['result'] = False
                result['messages'] = 'Error,node is not exit,please check node'
                result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/checknode?program=testprom&env=beta&node=testprom01.beta1.fn'
                print result
                self.write(json.dumps(result))

class createNodeHandler(tornado.web.RequestHandler):
    def get(self):
        prom = self.get_argument("program")
        env = self.get_argument("env")
        node = self.get_argument("node")
        result={}
        group = '  '+prom+'_'+env
        res = api(group=group,node=node)
        if not res.createNode():
            result['result'] = True
            result['messages'] = 'Success,create node '
            result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createnode?program=testprom&env=beta&node=testprom01.beta1.fn'
            print result
            self.write(json.dumps(result))
        elif res.checkAlive() is None:
            '''None - Remove node.conf nodes have been added '''
            apiUtils.createNode(group,node)
            result['result'] = True
            result['messages'] = 'Success,create node 1'
            result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createnode?program=testprom&env=beta&node=testprom01.beta1.fn'
            print result
            self.write(json.dumps(result))
        else:
            result['result'] = False
            result['messages'] = 'Info, node is exit'
            result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/createnode?program=testprom&env=beta&node=testprom01.beta1.fn'
            print result
            self.write(json.dumps(result))

class checkGroupHandler(tornado.web.RequestHandler):
    def get(self):
        prom = self.get_argument("program")
        env = self.get_argument("env")
        group = '  '+prom+'_'+env
        result = {}
        res = api(group=group)

        if res.checkGroup():
            result['result'] = True
            result['messages'] = 'Success,create group is ok'
            result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/checkgroup?program=testprom&env=beta'
            print result
            self.write(json.dumps(result))
        else :
            result['result'] = False
            result['messages'] = 'Error,Please check group'
            result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/checkgroup?program=testprom&env=beta'
            print result
            self.write(json.dumps(result))

class createGroupHandler(tornado.web.RequestHandler):
    def get(self):
        prom = self.get_argument("program")
        env = self.get_argument("env")
        soft = self.get_argument("soft")
        group = '  '+prom+'_'+env
        result = {}
        res = api(group=group,tgt=prom,soft=soft)
        '''create webserver/prom/prom'''
        if not res.checkGroup() and soft == 'php':
            '''create php group'''
            res.createGroup()
            res.createPhpFile()
            result['result'] = True
            result['messages'] = 'Success,create PHP group is ok'
            result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/creategroup?program=testprom&env=beta&soft=php'
            print result
            self.write(json.dumps(result))
        elif not res.checkGroup() and soft == 'java':
            '''create java group'''
            res.createGroup()
            res.createJavaFile()
            result['result'] = True
            result['messages'] = 'Success,create Java group is ok'
            result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/creategroup?program=testprom&env=beta&soft=java'
            print result
            self.write(json.dumps(result))
        else :
            result['result'] = False
            result['messages'] = "Info,Group already exists"
            result['documentation_url'] = 'http://10.202.184.248:9000/salt/v1/creategroup?program=testprom&env=beta&soft=[php|java|None]'
            print result
            self.write(json.dumps(result))
        
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/salt/v1/creategroup",createGroupHandler),
            (r"/salt/v1/createnode",createNodeHandler),
            (r"/salt/v1/createstate",runStateHandler),
            (r"/salt/v1/addnodestate",AddNodeStateHandler),
            (r"/salt/v1/createrundeck",createRundeckHandler),
            (r"/salt/v1/checkgroup",checkGroupHandler),
            (r"/salt/v1/checknode",checkNodeHandler),
            (r"/salt/v1/checkpillar",checkPillarHandler),
            (r"/salt/v1/checkphp",checkPHPHandler),
            (r"/salt/v1/checklogstash",checkLogstashHandler),
            (r"/salt/v1/checkzabbix",checkZabbixHandler),
            (r"/salt/v1/testping",testPingHandler),
       ],**settings
    )
    logging.debug("debug ...")
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
