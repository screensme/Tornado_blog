#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import motor
from tornado import gen
import time
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


class roothandler(tornado.web.RequestHandler):
    def get(self):
        blog_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        self.render("login.html")


class HomeHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        db=self.settings["db"]
        blogs=yield db.blog.find({}).to_list(100)
        self.render('home.html',blogs=blogs)

class BlogHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        blog_title=self.get_argument('title')
        blog_content=self.get_argument('content')
        db=self.settings['db']
        blog=yield db.blog.find_one({'title':blog_title,'content':blog_content})
        self.render('blog.html',blog=blog)

class Category_blogHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        category=self.get_argument('category')
        db=self.settings['db']
        Blogs=yield db.blog.find({'category':category}).to_list(100)
        self.render('category_blog.html',category=category,blogs=Blogs)



