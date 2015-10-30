#coding:utf-8
__author__ = 'Administrator'
import tornado.web
from tornado import gen

class SignUpHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def post(self):
        user=self.get_argument('username')
        password=self.get_argument('password')
        db=self.settings["db"]
        re =yield db.user.find_one({'SignUsername':user})
        if user :
            try:
                if re is not None:
                    self.write('<script>alert("用户名已经存在")</script>')
                    self.redirect('/home/signup')
                    return
                else:
                    db.user.insert({'SignUsername':user,'SignPassword':password})
                    self.write('<script>alert("注册成功")</script>')
                    self.redirect('/home/login')
            except:
                pass

        else:
            self.write("<script>alert('用户名不能为空')</script>")
            # self.redirect('/home/signup')

    def get(self):
        self.render("signup.html")