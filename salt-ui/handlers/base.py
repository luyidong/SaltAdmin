#!/usr/bin/env python
#coding=utf-8
#__author__  = louis,
# __date__   = 2016-04-20 01:12,
#  __email__ = yidongsky@gmail.com,
#   __name__ = base.py


import tornado.web
import  re
import json

from saltapi import SaltAPI
import settings


class indexDevops(tornado.web.RequestHandler):
    def get(self):
        #greeting = self.get_argument('greeting', 'Hello')
        #self.write(greeting + ', friendly user!')
        self.render("base/index.html")


class HelloModule(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello,world")


# class DataCenter(models.Model):
#     dcen = models.CharField(max_length=30, blank=True, verbose_name=u'机房简称')
#     dccn = models.CharField(max_length=30, blank=True, verbose_name=u'机房全称')
#
#     def __unicode__(self):
#         return u'%s %s' %(self.dcen, self.dccn)

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        saltapi = SaltAPI(
            url=settings.SALT_API['url'],
            username=settings.SALT_API['user'],
            password=settings.SALT_API['password']
        )
        minions, minions_pre, minions_rej,minions_den  = saltapi.allMinionKeys()
        #print minions_den
        return self.render( 'bases.html',minions_den=minions_den)


class AllkeysHandler(tornado.web.RequestHandler):
    def get(self):
        saltapi = SaltAPI(
            url=settings.SALT_API['url'],
            username=settings.SALT_API['user'],
            password=settings.SALT_API['password']
        )
        minions, minions_pre, minions_rej,minions_den  = saltapi.allMinionKeys()
        return self.render( 'base-minions.html',minions=minions)

class UnacceptkeysHandler(tornado.web.RequestHandler):
    def get(self):
        saltapi = SaltAPI(
            url=settings.SALT_API['url'],
            username=settings.SALT_API['user'],
            password=settings.SALT_API['password']
        )
        minions, minions_pre, minions_rej,minions_den  = saltapi.allMinionKeys()
        return self.render( 'base-unaccept.html',minions_pre=minions_pre)

class DeniedkeysHandler(tornado.web.RequestHandler):
    def get(self):
        saltapi = SaltAPI(
            url=settings.SALT_API['url'],
            username=settings.SALT_API['user'],
            password=settings.SALT_API['password']
        )
        minions, minions_pre, minions_rej,minions_den  = saltapi.allMinionKeys()
        res = {"data":minions_den}
        print res
        #self.write(json.dumps(res))
        return self.render( 'base-denied.html',minions_den=minions_den)

class RejectedkeysHandler(tornado.web.RequestHandler):
    def get(self):
        saltapi = SaltAPI(
            url=settings.SALT_API['url'],
            username=settings.SALT_API['user'],
            password=settings.SALT_API['password']
        )
        minions, minions_pre, minions_rej,minions_den  = saltapi.allMinionKeys()
        return self.render( 'base-rejected.html', minions_rej= minions_rej)



class deleteMinionKeysHandler(tornado.web.RequestHandler):
    '''
    删除已经接受的minion keys；
    :param request:
    :return:
    '''
    def get(self):
        minion_id = self.get_argument('minion_id')
        saltapi = SaltAPI(
            url=settings.SALT_API['url'],
            username=settings.SALT_API['user'],
            password=settings.SALT_API['password'])
        minions, minions_pre, minions_rej,minions_den  = saltapi.allMinionKeys()
        result = {}
        if minion_id.find(','):
            minion_id_list = minion_id.split(',')
            if set(minion_id_list).issubset(set(minions)):
                for id in minion_id_list:
                    result['result'] = saltapi.deleteKeys(id)
                    self.write(json.dumps(result))
            else:
                result['result'] = False
                self.write(json.dumps(result))
        elif minion_id in minions:
            result['result'] = saltapi.deleteKeys(minion_id)
            print result
            self.write(json.dumps(result))
        else:
            result['result'] = False
            print result
            self.write(json.dumps(result))
            #self.redirect("/salt/allkeys")

class acceptMinionKeysHandler(tornado.web.RequestHandler):
    '''
    Master将待接受的minion keys接受；
    :param request:
    :return:
    '''
    def get(self):
        minion_id = self.get_argument('minion_id')
        saltapi = SaltAPI(
            url=settings.SALT_API['url'],
            username=settings.SALT_API['user'],
            password=settings.SALT_API['password'])
        minions, minions_pre, minions_rej,minions_den  = saltapi.allMinionKeys()
        result = {}
        if minion_id.find(','):
            minion_id_list = minion_id.split(',')
            if set(minion_id_list).issubset(set(minions_pre)):

                for id in minion_id_list:
                    result['result'] = saltapi.acceptKeys(id)

                    self.write(json.dumps(result))
                self.redirect("/salt/unacceptkeys")
            else:
                result['result'] = False
                self.write(json.dumps(result))
                # for id in minion_id_list:
                #     print 'Error, %s is not in minions_pre ' % id
                self.redirect("/salt/unacceptkeys")


        elif minion_id in minions_pre:
            result['result'] = saltapi.acceptKeys(minion_id)
            print result
            self.write(json.dumps(result))
        else:
            result['result'] = False
            print result
            self.write(json.dumps(result))
            return
            #self.redirect("/salt/unacceptkeys")


class deleteRejectKeysHandler(tornado.web.RequestHandler):
    '''
    Master删除已经拒绝的minion keys;
    :param request:
    :return:
    '''
    def get(self):
        minion_id_list = self.get_argument('rejectkeys')
        minion_id_strings = ','.join(minion_id_list)
        saltapi = SaltAPI(
            url=settings.SALT_API['url'],
            username=settings.SALT_API['user'],
            password=settings.SALT_API['password'])
        ret = saltapi.deleteKeys(minion_id_strings)
        self.redirect("/salt/rejectedkeys")

class deletedeniedKeysHandler(tornado.web.RequestHandler):
    '''
    Master将已拒绝的minion keys接受；
    :param request:
    :return:
    '''
    def get(self):
        minion_id = self.get_argument('deniedkeys')
        saltapi = SaltAPI(
            url=settings.SALT_API['url'],
            username=settings.SALT_API['user'],
            password=settings.SALT_API['password'])

        result = {}
        result['result'] = saltapi.deleteKeys(minion_id)
        print result
        self.write(json.dumps(result))
        self.redirect("/salt/deniedkeys")