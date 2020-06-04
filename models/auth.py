# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 16:50
# @Author  : summer
# @File    : auth.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.db import Base, session
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))




class BaseModels:     #重写基类
    is_delete = Column(Boolean, default=False)  #逻辑删除
    update_time = Column(DateTime, default=datetime.now)     #修改时间
    create_time = Column(DateTime, default=datetime.now)    #创建时间




class User(Base, BaseModels):       #用户表
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(30), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    activation = Column(Boolean, default=False,)       #用户激活，默认不激活
    email = Column(String(50))
    mobile = Column(String(30), unique=True)

    @classmethod
    def add_user(cls, username, password, **kwargs):
        user = User(username=username, password=password, **kwargs)
        session.add(user)
        session.commit()
        session.close()


    @classmethod            #调用User类本身,查询user表
    def check_username(cls, username):
        return session.query(cls).filter_by(username=username).first()    #类本身进行查询

    def __repr__(self):
        return "User:username={},password={}".format(self.username, self.password)


#图片分类表
class PostType(Base, BaseModels):
    __tablename__ = "posttype"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))


class Post(Base, BaseModels):      #图片表
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))     #图片标题
    image_url = Column(String(300))     #图片地址
    content = Column(String(300))       #内容
    thumbnail_url = Column(String(300))     #缩略图

    user_id = Column(Integer, ForeignKey("users.id"))   #一对多外键关联
    user = relationship("User", backref="posts", uselist=False, cascade="all")    #backref=正反向查询

    posttype_id = Column(Integer, ForeignKey("posttype.id"))  # 一对多外键关联，图片分类表
    posttype = relationship("PostType", backref="p_type", uselist=False, cascade="all")  #backref=正反向查询



#图片实例.user ==>拿到对应的user实例
#用户实例.posts ==>拿到对应的图片实例

    def __repr__(self):
        return "Post:title={}".format(self.title)

    @classmethod
    def add_post(cls, title, content, image_url, thumbnail_url, username, posttype_id):
        user = User.check_username(username)    #返回 user实例
        post = Post(title=title, content=content, image_url=image_url, thumbnail_url=thumbnail_url, user_id=user.id, posttype_id=posttype_id)
        session.add(post)
        session.commit()
        session.close()


#评论表
class Comment(Base, BaseModels):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))       #关联评论者id
    post_id = Column(Integer, ForeignKey("posts.id"))       #关联评论图片的id
    reply_id = Column(Integer, ForeignKey("comment.id"))       #关联自己评论的id
    up = Column(Integer)        #点赞
    down = Column(Integer)      #踩一下
    content = Column(String(200))       #评论内容


