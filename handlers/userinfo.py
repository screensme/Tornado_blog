__author__ = 'Administrator'
class UserLoginInfo():
    def __init__(self,u,p,s):
        self.username_info=u
        self.password_info=p
        self.status_info=s
    def get_usernameinfo(self):
        return self.username_info
    def get_passwordinfo(self):
        return self.password_info
    def get_statusinfo(self):
        return self.status_info