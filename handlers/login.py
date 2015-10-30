__author__ = 'Administrator'
from handlers.BaseHandler import BaseHandler
import pymongo
import motor
class LoginHandler(BaseHandler):

    def post(self):
        username=self.get_argument('username')
        password=self.get_argument('password')
        db=self.settings['db']
        user=db.user.find({'SignUsername':username,'SignPassword':password})

        if user is None:
            UserName=db.user.find_one({'SignUsername':username})
            if UserName is not None:
                 self.write('<script>alert("password is wrong,try again")</script>')
                 self.render('login.html')
                 return
            elif UserName is None:
                self.write('<script>alert("user does not exist ,please Sign Up")</script>')
                return
        self.set_secure_cookie('username',username)

        self.redirect('/home')
    def get(self):
        username=self.get_secure_cookie('username')
        if username:
            self.redirect('/home')
        self.render('login.html')
