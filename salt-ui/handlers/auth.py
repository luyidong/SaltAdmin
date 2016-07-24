#!/usr/bin/env python
# coding=utf-8
# __author__  = louis,
# __date__   = 2016-04-27 17:54,
#  __email__ = yidongsky@gmail.com,
#   __name__ = auth.py

import bcrypt
import concurrent.futures
import tornado.escape
from tornado import gen
import tornado.httpserver
import tornado.ioloop
import tornado.web
import time


# A thread pool to be used for password hashing with bcrypt.
executor = concurrent.futures.ThreadPoolExecutor(2)


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie("fable_user")
        #print 'user ',user_id
        #print type(user_id)
        if not user_id: return None
        return self.db.get("SELECT * FROM user WHERE username = '%s'" % (user_id))

    def any_author_exists(self):
        return bool(self.db.get("SELECT * FROM user LIMIT 1"))


class Mainhandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('index.html',fable_user=self.get_current_user())


class AuthCreateHandler(BaseHandler):
    def get(self):
        try:
            errormsg = self.get_argument("error")
        except:
            errormsg = ""
        self.render("create_user.html", errormessage=errormsg)


    @gen.coroutine
    def post(self):
        # init login time
        t=int(time.time())
        last_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))
        '''
        active ＝  1 enable ／0 disable
        superuser ＝ 1 ture ／0 false
        role_id = 1 superuser / 2 admin /3 guest
        '''
        active = 0
        superuser = 0
        role_id = 3
        hashed_password = yield executor.submit(
            bcrypt.hashpw, tornado.escape.utf8(self.get_argument("password")),
            bcrypt.gensalt())

        author_id = self.db.execute("insert into user (username,email,hashed_password,nickname,last_login,\
                                is_active,is_superuser,role_id) Values ('%s','%s','%s','%s','%s','%s','%s','%s') " % \
                                (self.get_argument("username"),tornado.escape.utf8(self.get_argument("email")),\
                                 hashed_password,tornado.escape.utf8(self.get_argument("nickname")),\
                                 last_time,active,superuser,role_id)
                                )
        #print type(author_id)

        if not self.request.headers.get("Cookie"):return
        self.set_secure_cookie("fable_user", self.get_argument("username"))
        self.redirect(self.get_argument("next", "/"))


class AuthLoginHandler(BaseHandler):
    def get(self):
        # If there are no authors, redirect to the account creation page.
        if not self.any_author_exists():
            self.redirect("/auth/create")
        else:
            self.render("logins.html", error=None)

    @gen.coroutine
    def post(self):

        author = self.db.get("SELECT * FROM user WHERE username = '%s'" %
                    self.get_argument("username"))
        print author
        if not author:
            self.render("logins.html", error="username not found")
            return
        hashed_password = yield executor.submit(
            bcrypt.hashpw, tornado.escape.utf8(self.get_argument("password")),
            tornado.escape.utf8(author.hashed_password))
        #print hashed_password
        if hashed_password == author.hashed_password:
            self.set_secure_cookie("fable_user", self.get_argument("username"))
            self.redirect(self.get_argument("next", "/"))
        else:
            self.render("logins.html", error="incorrect password")


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("fable_user")
        self.redirect(self.get_argument("next", "/"))


