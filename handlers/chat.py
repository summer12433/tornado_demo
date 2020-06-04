# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 23:08
# @Author  : summer
# @File    : chat.py

import tornado.websocket
import tornado.web

from .main import BaseHandler   #导入basehandler类

class RoomHandler(BaseHandler):
    """
    聊天室
    """
    @tornado.web.authenticated
    def get(self):
        return self.render("room.html")


class EchoWebSocket(tornado.websocket.WebSocketHandler, BaseHandler):
    """
    处理信息
    """
    waiters = set()     #接收每一个用户

    def open(self):
        EchoWebSocket.waiters.add(self)
        for w in EchoWebSocket.waiters:
            w.write_message(u"%s 进入教室: " % self.current_user)


    def on_message(self, message):
        for w in EchoWebSocket.waiters:
            w.write_message(u"%s: %s" %(self.current_user, message))

    def on_close(self):
        EchoWebSocket.waiters.remove(self)
        for w in EchoWebSocket.waiters:
            w.write_message(u"%s 退出教室: " % self.current_user)





