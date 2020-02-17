#!/usr/local/bin/python3
# encoding:utf-8
'''
@File    :   生成随机激活码.py
@Time    :   2020/02/14 16:12:23
@Author  :   WXL-c137
@Version :   1.0
@Contact :   844577557@qq.com
@WebSite :   null
'''
# Start typing your code from here
import string
import random

code = string.ascii_letters + string.digits
# print(code)


def getCode():
    return "".join(random.sample(code, 4))


# print(getCode())


def key(group):
    return "—".join([getCode() for i in range(group)])


# print(key(4))


def keys(n):
    return "\n".join([key(4) for i in range(n)])


print(keys(200))