# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 16:50
# @Author  : summer
# @File    : db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


HOSTNAME = '47.100.201.79'
PORT = '3306'
DATABASE = 'instagram'
USERNAME = 'summer'
PASSWORD = 'qwe123'


db_url = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
    USERNAME,
    PASSWORD,
    HOSTNAME,
    DATABASE,
)

engine = create_engine(db_url)

Base = declarative_base(engine)


Session = sessionmaker(engine)
session = Session()

if __name__=='__main__':
    print(dir(Base))
    print(dir(session))
