#coding:utf-8
__author__ = 'Screensme'

from handlers import every_handlers
from handlers import edit
from handlers import logout
from handlers import login
from handlers import signup
from handlers import userinfo

handlers=[
    (r'/',every_handlers.roothandler),#首页
    (r'/home',every_handlers.HomeHandler),   #个人后台管理页
#    (r'/home/manage_list',),#个人后台管理（已发布博客列表）
    (r'/home/edit',edit.edithandler),#写博客页
    (r'/home/blog_manage/(\w+)',every_handlers.BlogHandler),#个人后台博客编辑页
    (r'/home/blog/(\w+)',every_handlers.BlogHandler),
    (r'/home/category_blog',every_handlers.Category_blogHandler),
    (r'/home/signup',signup.SignUpHandler),
    (r'/home/login',login.LoginHandler),
    (r'/home/logout', logout.LogOutHandler),
]

# 首页
# 个人后台管理页
# 个人后台管理（已发布博客列表）
# 写博客页
# 个人后台博客编辑页
# 博客种类
# 注册-->登录
# 登录-->个人后台管理页
# 退出-->登录
