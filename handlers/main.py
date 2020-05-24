# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 16:00
# @Author  : summer
# @File    : main.py


import tornado.web      #导入web接口
from pycket.session import SessionMixin
import os
from models.auth import Post
from models.db import session

class BaseHandler(SessionMixin, tornado.web.RequestHandler):
    def get_current_user(self):
        return self.session.get("user")



class IndexHandler(tornado.web.RequestHandler):
    """
    首页 用户上传图片展示
    """
    def get(self):
        posts = session.query(Post).all()  # 获取所有的图片
        return self.render("index.html", posts=posts)

class ExporeHandler(tornado.web.RequestHandler):
    """
    最近上传的图片页面
    """
    def get(self):
        return self.write("最近上传图片页面")


class PostHandler(tornado.web.RequestHandler):
    """
    单个图片的详情页面
    """
    def get(self, post_id):     #传入图片对应id
        return self.write("详情页")


class UpdateHandler(BaseHandler):
    """
    图片上传
    """
    @tornado.web.authenticated      #用户必须登录 装饰器
    def get(self):
        return self.render("update.html")

    @tornado.web.authenticated
    def post(self):
        upload_path = "static/upload"   #配置上传路径
        file_metas = self.request.files.get("image_file", []) #获取上传图片

        #写入文件
        for meta in file_metas:
            file_name = meta.get("filename")    #获取文件名
            file_path = os.path.join(upload_path, file_name)    #拼接上传路径
            with open(file_path, "wb") as up:
                up.write(meta.get("body"))      #写入文件内容

            #入库
            # print(self.current_user)     #获取当前用户用户名
            Post.add_post("upload/{}".format(file_name), self.current_user)
            return self.write("上传成功")















