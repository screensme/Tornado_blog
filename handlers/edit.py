# -*- coding: utf-8 -*-
import time
import logging
from PIL import Image
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo

class edithandler(tornado.web.RequestHandler):
    def get_img(self):
        if self.request.files=={} or 'img' not in self.request.files:
            self.write('<script>alert("select a image")</script>')
            error=1
            return error
        image_type_list = ['image/gif', 'image/jpeg',
                           'image/bmp', 'image/png', 'image/x-png']
        img=self.request.files['img'][0]

        if img['content_type'] not in image_type_list:
            self.write('<script>alert("only jpg,jpeg,bmp,gif,png!")</script>')
            error=1
            return error
        if len(img['body']) > 4*1024*1024:
            self.write('<script>alert("the max size is upon4M");</script>')
            error=1
            return error
        temp_file = open("temp_image",'wb+')
        temp_file.write(img['body'])
        temp_file.seek(0)
        try:
            image_one=Image.open(temp_file.name,'r')
        except IOError,error:
            logging.info(error)
            logging.info(self.request.headers)
            temp_file.close()
            self.write('<script>alert("cannot upload this kind of image")</script>')
            error=1
            return error
        if image_one.size[0] < 250 or image_one.size[1] < 250 or \
                        image_one.size[0] > 2000 or image_one.size[1] > 2000:
            self.write('<script>alert("size is about 250px~2000px")</script>')
            error=1
            return error
        image_path = "./static/picture/"
        image_format = img['filename'].split('.').pop().lower()
        image_format=image_one.format
        tmp_name = image_path + str(int(time.time())) +'.'+ image_format
        image_one.save(tmp_name,image_format)
        temp_file.flush()
        temp_file.close()
        self.write('<script>alert("image upload successful the path is:" + image_path[1:])</script>')
        return tmp_name

    def post(self):
        blog_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        title=self.get_argument("title")
        tag=self.get_argument("tag")
        content=self.get_argument("content")
        category=self.get_argument("classify")
        status=self.get_argument("status")
        img_link=self.get_img()
        db=self.settings['db']
        if img_link==1:
            db.blog.insert({'time':blog_time,'title':title,'tag':tag,'content':content,'img_link':1,'category':category,'status':status})
            self.write('<script>alert("upload blog successful,but image cannot be uploaded,please try again")</script>')
        else:
            db.blog.insert({'time':blog_time,'title':title,'tag':tag,'content':content,'img_link':img_link,'category':category,'status':status})
            self.write('<script>alert("upload blog successful")</script>')
        self.redirect('/home')

    def get(self):
        self.render('edit.html')