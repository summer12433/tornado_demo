# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 16:00
# @Author  : summer
# @File    : main.py
import uuid
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

import tornado.web      #导入web接口
from PIL import Image
from pycket.session import SessionMixin
import os
from models.auth import Post, PostType
from models.db import session


class BaseHandler(SessionMixin, tornado.web.RequestHandler):
    def get_current_user(self):
        return self.session.get("user")

@gen.coroutine
def asy_update():
    # yield gen.sleep(5)
    # http_client = AsyncHTTPClient()     #异步HTTP客户端对象
    # response = yield http_client.fetch(url)     #获取异步结果
    # raise gen.Return(response)
    posttype_all = session.query(PostType).all()
    raise gen.Return(posttype_all)


class IndexHandler(BaseHandler):
    """
    首页 用户上传图片展示
    """
    def get(self):
        posts = session.query(Post).all()  # 获取所有的图片
        # p_type = session.query(PostType).all()  #获取文章类型
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
        posts = session.query(Post).get(post_id)
        type_all = session.query(PostType).all()        #查询全部图片标签
        if not posts:
            return self.write_error(404)        #查不到超出的图片id就返回404页面
        return self.render("single.html", posts=posts, type_all=type_all)


class UpdateHandler(BaseHandler):
    """
    图片上传
    """
    @gen.coroutine
    @tornado.web.authenticated      #用户必须登录 装饰器
    def get(self):
        # response = yield asy_update("http://47.100.201.79:8888/update")
        # return self.write(response.body)
        # posttype_all = session.query(PostType).all()
        # return self.render("update.html", posttype_all=posttype_all)
        posttype_all = yield asy_update()
        return self.render("update.html", posttype_all=posttype_all)


    @tornado.web.authenticated
    def post(self):
        title = self.get_argument("title", "")      #获取前端输入的值
        content = self.get_argument("content", "")

        upload_path = "static/upload"   #配置上传路径
        file_metas = self.request.files.get("image_file", []) #获取上传图片

        #写入文件
        for meta in file_metas:
            image_type =meta.get("filename").split(".")[-1]     #获取后缀名
            file_name = str(uuid.uuid1()) + "." + image_type    #构造文件名
            file_path = os.path.join(upload_path, file_name)    #拼接上传路径
            with open(file_path, "wb") as up:
                up.write(meta.get("body"))      #写入文件内容

            #缩略图
            im = Image.open(file_path)  #打开图片
            im.thumbnail((256.69, 270))
            im.save(file_path, image_type if image_type == "png" else "JPEG")

            thumbnail_url = "upload/thumbnail/{}".format(file_name)     #缩略图保存地址
            #入库
            # print(self.current_user)     #获取当前用户用户名
            Post.add_post(title, content, "upload/{}".format(file_name), thumbnail_url, self.current_user, 3)
        return self.write("上传成功")















