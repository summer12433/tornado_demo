# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 16:00
# @Author  : summer
# @File    : main.py


import tornado.web      #导入web接口


class IndexHandler(tornado.web.RequestHandler):
    """
    首页 用户上传图片展示
    """
    def get(self):
        return self.write("首页")

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






