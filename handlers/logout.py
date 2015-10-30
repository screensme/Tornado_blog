
from handlers.BaseHandler import BaseHandler

class LogOutHandler(BaseHandler):
    def get(self):
        self.clear_cookie('username')
        self.redirect('/home/login')
