# -*- coding: utf-8 -*-
# @Time    : 2020/5/23 20:13
# @Author  : summer
# @File    : account.py

from bcrypt import hashpw, gensalt

#加密
def pas_encryption(pwd, passwd=None, b=True):     #b=True这个类默认true加密，false解密
    #passwd = None      加密之后的密码
    if b:
        # 这个是随机生成的盐
        salt = gensalt(12)

        # 这个是通过盐去加密
        passwd = hashpw(pwd.encode('utf8'), salt)
        return passwd
    else:
        # 将输入的明文密码与密文密码进行加密，是否等于密文密码。
        return hashpw(pwd.encode('utf8'), passwd.encode("utf8"))






