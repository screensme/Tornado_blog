#coding:gbk
import os
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo
import motor
from tornado.options import define,options
import Hand_lers

define("port",default=8000,help="run on the given port",type=int)

client=motor.MotorClient("localhost",27017)
db=client.blog
settings={
    'template_path':os.path.join(os.path.dirname(__file__),"templates"),
    'static_path':os.path.join(os.path.dirname(__file__),"static"),
    'debug':True,
    'db':db,
    'cookie_secret':'wuy342iu34y2i3uy23uiy23sesd'
}

if __name__=='__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=Hand_lers.handlers,**settings)
    http_server=tornado.httpserver.HTTPServer(app,xheaders=True)#获取客户端IP(xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()