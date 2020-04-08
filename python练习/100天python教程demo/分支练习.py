#!/usr/local/bin/python3
# encoding:utf-8
'''
@File    :   分支练习.py
@Time    :   2020/04/08 21:21:18
@Author  :   WXL-c137
@Version :   1.0
@Contact :   844577557@qq.com
@WebSite :   null
'''
# Start typing your code from here

# 厘米英寸单位转换

value = float(input('请输入单位长度： '))
unit = input('请输入长度单位：')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效单位')
