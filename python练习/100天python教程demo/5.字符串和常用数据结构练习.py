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
