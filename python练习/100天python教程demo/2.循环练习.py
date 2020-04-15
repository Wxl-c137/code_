#!/usr/local/bin/python3
# encoding:utf-8
'''
@File    :   2.循环练习.py
@Time    :   2020/04/09 11:40:40
@Author  :   WXL-c137
@Version :   1.0
@Contact :   844577557@qq.com
@WebSite :   null
'''
# Start typing your code from here

# 输入一个正整数判断它是不是素数
""" from math import sqrt

num = int(input('请输入一个正整数'))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d 不是素数' % num) """

# 输入两个正整数计算它们的最大公约数和最小公倍数
""" x = int(input('x = '))
y = int(input('y = '))

if x > y:
    x, y = y, x

for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break """

# 打印如下所示的三角形图案
""" row = int(input('请输入行数'))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print() """
