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
""" value = float(input('请输入单位长度： '))
unit = input('请输入长度单位：')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效单位')
 """

# 根据分数判断等级
""" score = int(input('请输入你的分数： '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('你的等级为:', grade) """

#输入三条边长，如果能构成三角形就计算周长和面积。
a = float(input('请如边长a:'))
b = float(input('请如边长b:'))
c = float(input('请如边长c:'))
if a + b > c and a + c > b and b + c > a:
    print('周长:%f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c))**0.5
    print('面积： %f' % (area))
else:
    print('不能组成三角形')