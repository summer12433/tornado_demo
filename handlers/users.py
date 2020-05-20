# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 16:17
# @Author  : summer
# @File    : users.py

import tornado.web      #导入web接口
from models.auth import User
import os

class RegisterHandler(tornado.web.RequestHandler):
    """
    注册功能
    """
    def get(self):
        return self.render("register.html")

    def post(self):
        """
        1. 获取前端参数
        2.效验参数
        3.入库
        4.返回数据
        :return:
        """
        username = self.get_argument("username", "").strip()    #strip去掉空格
        password = self.get_argument("password", "").strip()
        repeat_password = self.get_argument("repeat_password", "").strip()

        if not all([username, password, repeat_password]):    #判断是否为空，接收列表
            return self.write("参数错误")       #return结束函数不执行

        if not (len(username) >= 6 and len(password) >= 6 and password==repeat_password):       #判断用户名密码长度
            return self.write("格式错误")

        if User.check_username(username):   #判断用户唯一，调用User类查询
            return self.write("用户名已存在")

        #加密


        try:
            User.add_user(username, password)   #存入数据
            return self.redirect("/login")
        except Exception as e:
            print(e)









class LoginHandler(tornado.web.RequestHandler):
    """
    登录
    """

    def get(self):
        return self.render("login.html")

    def post(self):
        pass












