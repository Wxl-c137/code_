# 在屏幕上显示跑马灯文字
"""
import os
import time


def main():
    content = '北京第三交通提醒您~行车千万条，安全第一条。行车不规范，亲人两行泪！......'
    while True:
        os.system('cls')
        print(content)

        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == "__main__":
    main()
 """

# 设计一个函数产生制定长度的验证码，验证码由大小写字母和数字构成
""" import random
import string


def generat_code(code_len=4):
    all_char = string.ascii_letters + string.digits
    last_pos = len(all_char) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_char[index]
    print(code)


generat_code() """

# 获取文件后缀的函数
"""

def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''  """

# 设计一个函数返回传入列表中最大和第二大的数
"""  
def max2(x):
    m1, m2 = (x[0], x[1] if x[0] > x[1] else (x[1], x[0]))
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2
 """

#  计算指定年月日是这一年的第几天

year = int(input('请输入年份：'))
month = int(input('请输入月份：'))
day = int(input('请输入日期：'))

# def leapyear(year):
if year%4 == 0:
    febdays = 29
else:
    febdays = 28
return febdays

month_list = [31, febdays, 31, 30, 31, 30, 31, 31, 30, 31, 31, 30]


# def day_nums(month, day):
if month > 1:
    for i in range(month):
        counts += month_list[i - 1]
    coutns = counts + day
    return counts
else:
    counts = day
    return counts

print('这是%d年的第%d天'%(year,counts)
