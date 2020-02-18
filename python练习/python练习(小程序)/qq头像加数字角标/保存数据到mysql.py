#!/usr/local/bin/python3
# encoding:utf-8
'''
@File    :   保存数据到mysql.py
@Time    :   2020/02/17 22:24:39
@Author  :   WXL-c137
@Version :   1.0
@Contact :   844577557@qq.com
@WebSite :   null
'''
# Start typing your code from here
from random import choice
import string
import pymysql.cursors


def get_code(dict, length, count):
    # 根据给定字典，长度来得出激活码
    for i in range(1, int(count) + 1):
        code = ""
        # 通过count限制激活码个数，循环调用choice来计算激活码
        for l in range(0, int(length)):
            code = code + str(choice(dict))
        save_to_mysql(i, code)


def save_to_mysql(id, code):
    # 将数据保存到mysql数据库
    host = ("localhost")
    user = ("root")
    pass_ = ("ayanamirie000")
    db = ("test database")
    #  设置数据库连接相关信息
    connect = pymysql.connect(host, user, pass_, db)
    cursor = connect.cursor()
    #  链接数据库并设置游标
    # sql_1 = "CREATE TABLE activeCode (id INT PRIMARY KEY,code varchar(255) )"
    sql = "insert into activeCode(id, code) VALUES ('%d', '%s');"
    data = (id, code)
    # cursor.execute(sql_1)
    cursor.execute(sql % data)
    # 执行sql语句


if __name__ == "__main__":
    dict = string.ascii_letters[:]
    # 设定字典为'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = input("请输入激活码个数：")
    if count == "":
        count = "1"
    length = input("请输入激活码长度：")
    if length == "":
        length = "8"
    get_code(dict, length, count)
