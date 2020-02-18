#!/usr/local/bin/python3
# encoding:utf-8
'''
@File    :   111.py
@Time    :   2020/02/18 14:50:38
@Author  :   WXL-c137
@Version :   1.0
@Contact :   844577557@qq.com
@WebSite :   null
'''
# Start typing your copride from here
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pymysql

conn = pymysql.connect(  # 创建数据库连接
    host='localhost',  # 要连接的数据库所在主机ip
    user='root',  # 数据库登录用户名
    password='ayanamirie000',  # 登录用户密码
    database='test_db',  # 连接的数据库名，也可以后续通过cursor.execture('user test_db')指定
    charset='utf8'  # 编码，注意不能写成utf-8
)

cursor = conn.cursor()  # 创建一个游标

# 需要执行的创建表的sql语
cursor.execute('select * from book where bookid < %s;', [4])
books = cursor.fetchall()
print(books)
# 执行完之后别忘了关闭游标和数据库连接
cursor.close()
conn.close()