# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 15:52
# @Author  : summer
# @File    : photo.py

import tornado.web

class PhotographyHandler(tornado.web.RequestHandler):
    """
    摄影
    """
    def get(self):
        return self.render("photography.html")



class TravelHandler(tornado.web.RequestHandler):
    """
    旅行
    """
    def get(self):
        return self.render("travel.html")

class FashionHandler(tornado.web.RequestHandler):
    """
    时尚
    """
    def get(self):
        return self.render("fashion.html")


class AboutHandler(tornado.web.RequestHandler):
    """
    关于我
    """
    def get(self):
        return self.render("about.html")


class ContactHandler(tornado.web.RequestHandler):
    """
    联系我
    """
    def get(self):
        return self.render("contact.html")