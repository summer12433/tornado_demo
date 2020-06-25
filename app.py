# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 15:40
# @Author  : summer
# @File    : app.py

import os
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options   #导入manage.py命令行
from handlers.main import IndexHandler, ExporeHandler, PostHandler, UpdateHandler
from handlers.users import RegisterHandler, LoginHandler
from handlers.photo import PhotographyHandler, TravelHandler, FashionHandler, AboutHandler, ContactHandler
from handlers.chat import RoomHandler, EchoWebSocket


define("port", default="8888", help="Listening port", type=int)     #配置信息

class Application(tornado.web.Application):  #继承tornado.web.Application
    def __init__(self):     #重写初始化类
        handlers = [        #路由
            (r"/", IndexHandler),       #首页
            (r"/expore", ExporeHandler),    #最近上传页面
            (r"/post/(?P<post_id>[0-9]+)", PostHandler),    #图片详情
            (r"/register", RegisterHandler),    #注册
            (r"/login", LoginHandler),      #登录
            (r"/update", UpdateHandler),    #图片上传
            (r"/photo", PhotographyHandler),    #摄影
            (r"/travel", TravelHandler),    #旅行
            (r"/fashion", FashionHandler),    #时尚
            (r"/about", AboutHandler),    #关于我
            (r"/contact", ContactHandler),    #联系我
            (r"/room", RoomHandler),    #在线咨询
            (r"/echoweb", EchoWebSocket),
        ]
        settings = dict(    #配置文件
            debug=True,
            template_path = "template",  # 配置模板路径
            static_path = "static",     #配置静态文件路径
            login_url = "/login",       #判断用户登录验证
            xsrf_cookies = True,
            cookie_secret = "dafhjfhjbnckjlhh",
            pycket={
                'engine': 'redis',
                'storage': {
                    'host': '127.0.0.1',  # 本地ip地址
                    'port': 6379,  # redis端口
                    'db_sessions': 10,  # 使用10号库
                    'max_connections': 2 ** 31,  # 设置字节长度
                    },
                    'cookies': {
                        # 设置过期时间
                        'expires_days': 2,
                        # 'expires':None, #秒
                        },
                    },
                )
        super().__init__(handlers, **settings)  #继承父类init方法


if __name__ == "__main__":
    tornado.options.parse_command_line()    #命令行
    application = Application()       #实例化类
    application.listen(options.port)    #绑定端口
    tornado.ioloop.IOLoop.current().start()     #开启服务