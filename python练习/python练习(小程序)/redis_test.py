# !/usr/local/bin/python3
# encoding:utf-8'''
'''
@File    :   redis.py
@Time    :   2020/02/19 13:04:32
@Author  :   WXL-c137
@Version :   1.0
@Contact :   844577557@qq.com
@WebSite :   null
'''
# Start typing your code from here

from redis import ConnectionPool
import redis
from redis_db0 import POOl
POOL = ConnectionPool(host='127.0.0.1', port=6379, max_connections=100)
conn = redis.Redis(connection_pool=POOl)
conn.set('name', 'LinWOW')
print(conn.get('name')