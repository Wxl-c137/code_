""" 
# 英制单位与公制单位
from random import randint
value = float(input('请输入长度'))
unit = input('请输入单位')

if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = % f英寸' % (value, value / 2.54))
else:
    print('请输入单位')

# 掷色子决定做什么事
face = randint(1, 6)

if face == 1:
    reslut = '唱歌'
elif face == 2:
    reslut = '跳舞'
elif face == 3:
    reslut = '学狗叫'
elif face == 4:
    reslut = '做俯卧撑'
elif face == 5:
    reslut = '念绕口令'
else:
    reslut = '讲个冷笑话'

print(reslut) """

""" # 百分制成绩转成等级制

score = float(input('请输入成绩： '))

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

print('你的等级是:', grade) """

""" # 输入三条边长 判断能否构成三角形，并计算周长和面积


import math
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and b + c > a and a + c > b:
    print('周长： %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积：%f' % (area))
else:
    print('不能组成三角形') """

# 个人所得随计算器
salary = float(input('本月收入: '))
insurance = float(input('五险一金: '))
diff = salary - insurance - 3500
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 4500:
    rate = 0.1
    deduction = 105
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 55000:
    rate = 0.3
    deduction = 2755
elif diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505
tax = abs(diff * rate - deduction)
print('个人所得税: ￥%.2f元' % tax)
print('实际到手收入: ￥%.2f元' % (diff + 3500 - tax))
