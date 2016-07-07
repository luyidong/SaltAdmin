# cat saltapiUtils.py
#!/usr/bin/env python
#coding=utf-8
#__author__  = louis,
# __date__   = 2016-06-06 17:16,
#  __email__ = yidongsky@gmail.com,
#   __name__ = saltapiUtils.py

import json
import sys,os
import commands
reload(sys)
sys.setdefaultencoding('utf8')

import salt.client as client

class api(object):
    def __init__(self,group=None,env=None,node=None,arg=None,soft=None,tgt=None):
        self.group = group #指定项目组www
        self.env = env     #环境beta dev preview online
        self.node = node   #Ex.test1.idc1.fn or test1.idc1.fn,test2.idc2.fn...
        self.arg = arg     #参数
        self.soft = soft   #指定软件类型php java logstash zabbix
        self.tgt = tgt     #额外预留参数 这里主要用在 创建salt对应项目的文件目录

    ''''test.ping'''
    def testPing(self):
        c = client.LocalClient()
        result=c.cmd(self.node,  # target 
            'test.ping',         # function
              timeout='15'
              )
        node_item = self.node.split(',')
        for i in node_item:
            for k,v in result.items():
                for n in node_item:
                    if k == i and v:
                        return True
                    else:
                        return False

    '''创建Java rundeck文件 '''
    def createRundeck(self):
        c = client.LocalClient()
        #item = '/bin/bash /var/rundeck/newjobimport.sh %s %s' %(self.group,self.env)
        item = 'source /etc/profile;sh /var/xxx/runjobimport.sh %s %s' %(self.group,self.env)
        result=client.LocalClient().cmd('run01.xxx.xxx','cmd.run',[item],timeout=15,verbose=True).items()
        for k,v in result:
                if v == 'ok':
                    return True
                else:
                    return False

    '''创建PHP salt文件 '''
    def createPhpFile(self):
        cmd="ls -l /usr/local/src/salt/webserver|awk {'print $NF'}|grep -v [0-9][0-9][0-9]|grep '^%s$' " % self.tgt
        info = commands.getoutput(cmd)
        if len(info):
            '''This progrom is existed! '''
            return False
        else:
            #idc1
            #(status, output) = commands.getstatusoutput("/usr/local/src/saltinit-php.sh %s "%(self.tgt))
            #idc2
            (status, output) = commands.getstatusoutput("/usr/local/src/saltinit-php.sh %s "%(self.tgt))
            return True

    '''创建Tomcat salt文件 '''
    def createJavaFile(self):
        cmd="ls -l /usr/local/src/salt/webserver|awk {'print $NF'}|grep -v [0-9][0-9][0-9]|grep '^%s$' " % self.tgt
        info = commands.getoutput(cmd)
        if len(info):
            '''This progrom is existed! '''
            return False
        else:
            (status, output) = commands.getstatusoutput("/usr/local/src/saltinit.sh %s "%(self.tgt))
            return True

    '''推送新增节点sls配置'''
    def AddNodeState(self):
        c = client.LocalClient()
        jid = ''
        node_item = self.node.split(',')
        for item in node_item:

            jid = c.cmd_async(item,  # target 
                'state.sls',         # function
                [self.arg],          # arg for function
                jid=jid,
                timeout='15',
                kwarg={'pillar':{'status':'TEST'},}
                )
            return jid

    '''推送sls配置'''
    def runState(self):
        c = client.LocalClient()
        jid = ''
        jid = c.cmd_async(self.group,  # target 
          'state.sls',                 # function
          [self.arg],                  # arg for function
          jid=jid,
          expr_form='nodegroup',
          kwarg={'pillar':{'status':'TEST'},}
          )
        return jid

    def checkPHP(self):
        c = client.LocalClient()
        result = c.cmd(self.group,  # target 
          'cmd.run',                # function
          ['php -m|wc -l'],         # arg for function
          expr_form='nodegroup',
          kwarg={'pillar':{'status':'TEST'},}
          ) 

        node_item = self.node.split(',')
        for k,v in result.items():
            for n in node_item:
                if k == n and v == '72':
                    return True
                else:
                    return False

    def checkLogstash(self):
        c = client.LocalClient()
        result = c.cmd(self.group,  # target 
          'cmd.run',                # function
          ['ps -elf|grep -w logstash|grep -v grep|wc -l'],  # arg for function
          expr_form='nodegroup',
          )
        node_item = self.node.split(',')
        for k,v in result.items():
            for n in node_item:
                if k == n and v >= '1':
                    print 'True'
                    return True
                else:
                    print 'False'
                    return False

    def checkZabbix(self):
        c = client.LocalClient()
        result = c.cmd(self.group,  # target 
          'cmd.run',    # function
          ['ps -elf|grep -w zabbix|grep -v grep|wc -l'],  # arg for function
          expr_form='nodegroup',
          kwarg={'pillar':{'status':'TEST'},}
          )
        node_item = self.node.split(',')
        for k,v in result.items():
            for n in node_item:
                if k == n and v >= '1':
                    return True
                else:
                    return False

    '''检测pillar'''
    def checkPillar(self):
        result = {}
        item = self.node.split(',')
        for i in item:
            if self.group and i:
                try:
                   result=client.LocalClient().cmd(self.group,'pillar.items',expr_form='nodegroup',timeout=15,verbose=True).items()
                   for k,v in result:
                       if i == k and len(v) != 0:
                           return True
                       else:
                          return False
                except:
                    return False

    '''判断组是否存在'''
    def checkGroup(self):
        count = 0
        with open("/etc/salt/master.d/node.conf") as f:
            for line in f:
                parts = line.split(':')
                if self.group in parts[0]:
                    count +=1
        f.close()

        if int(count) == 1:
            return True
        else:
            return False

    '''添加组'''
    def createGroup(self):
        f = open("/etc/salt/master.d/node.conf",'a')
        newgroup= self.group+':'+' L@'
        f.write(str(newgroup))
        f.close


    '''判断节点是否存在'''
    #已被checkAlive替换
    def checkNode(self):
       result = {}
       q_group = self.group
       print q_group
       if q_group:
           try:
               result=client.LocalClient().cmd(q_group,'cmd.run',[''],expr_form='nodegroup',timeout=15,verbose=True)
               print result.keys()
               exit_item = result.keys()
               node_item = self.node.split(',')
               for n in node_item:
                    if n in exit_item:
                        return True
           except:
               result['result'] = False
               return False
    

    '''判断节点是否存在'''
    def checkAlive(self):
        nodeList = self.node.split(',')
        exitLists = []
        with open("/etc/salt/master.d/node.conf") as f:
            for line in f:
                lines  = line.split(':')
                if len(lines) > 1 and self.group == lines[0]:
                        exitList =  lines[1][3:]
                        exitNode = exitList.split(',')
                        listNode = ['\n']
                        if exitNode == listNode or exitNode == '':
                            return False
                        else:
                            for eo in exitNode:
                                exitLists.append(eo.strip())

                else: 
                    # node list null
                    return False

        for inode in nodeList:
            print 'inode',len(inode),inode
            if inode in exitLists:
                return True
            else:
                return False

    '''添加节点'''
    def createNode(self):
       if self.group and self.node:
           nodeList = self.node.split(',')

           '''统计当前组节点数量,读取组节点列表'''
           nodelist_count =0
           node_count = 0
           res = []
           nodenum = len(nodeList)
           
           exitList = []
           with open("/etc/salt/master.d/node.conf") as f:
               for line in f:
                   #取第一列带空格匹配
                   lines  = line.split(':')
                   if len(lines) > 1 and self.group == lines[0]:
                       nl =  lines[1][3:]
                       nodeLen = len(nl)
                       exit_node = nl.split(',')
                       #避免节点列表如果为空，长度为1
                       nodeNull = ['\n']
                       if exit_node == nodeNull:
                            print 'list is Null'
                       else:
                           for item in exit_node:
                               exitList.append(item.strip())

                       for n in nodeList:
                           if n in exitList:
                               node_count = 0
                           elif nodeLen == 0 and nodenum == 1:
                               node_count = 0
                               res.append(n)
                           elif nodeLen == 0 and nodenum > 1:
                               node_count = 2
                               res.append(n)
                           else:
                               node_count += 1
                               res.append(n)

                       if exit_node == nodeNull or exit_node == ['']:
                           nodelist_count = 0
                       else:
                           for e in exitList:
                               for inode in nodeList:
                                   if inode == e:
                                       print 'ok',inode
                                       nodelist_count = 0
                                   else:
                                       nodelist_count =+1
                   else: 'Null'
           rest = ",".join(str(i) for i in res)
           for i in nodeList:
               '''根据节点元素判断节点是否在列表中'''
               if i in exitList:
                   return True
               else:
                   #将文件中的每行读取到list中，遍历list，对需要修改的某行进行修改
                   _list_content = [];
                   fh = open("/etc/salt/master.d/node.conf", 'rb')
                   for goup in fh.readlines():
                       _list_content.append(goup)
                   fh.close()
        
                   _content = ''
                   for item in _list_content:
                       group_item =self.group+':'
                       if group_item in item:
    
                           '''node.conf节点数 与新加节点数 判断'''
                       
                           #已存在节点，新增节点1
                           if nodelist_count == 0 and node_count == 1 :
                               item = '  '+item.strip()+rest.strip(',')+'\n'
                           #不存在节点，新增节点1
                           elif nodelist_count == 0 and node_count == 0 :
                               item = '  '+item.strip()+rest.strip(',')+'\n'
                           #不存在节点，新增节点1
                           elif nodelist_count == 1 and node_count == 0 :
                               item = '  '+item.strip()+rest.strip(',')+'\n'
                           #不存在节点，新增节点>1
                           elif nodelist_count == 0 and node_count > 1 :
                               item = '  '+item.strip()+rest.strip(',')+'\n'
                           #已存在节点，新增节点1
                           elif nodelist_count == 1 and node_count == 1 :
                               item = '  '+item.strip()+ ','+rest.strip(',')+'\n'
                           #已存在节点，新增节点>1
                           elif nodelist_count == 1 and node_count > 1 :
                               item = '  '+item.strip()+ ','+rest.strip(',')+'\n'
                           else:
                               #print 'Error'
                               return False
                        
                       _content = _content + item
                  
                   open('/etc/salt/master.d/node.conf', 'wb').writelines(_content)
