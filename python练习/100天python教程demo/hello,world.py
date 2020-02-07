# 给出半径求园的周长和面积
# 华氏度转换为摄氏度
import math

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

radius = float(input('请输入园的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)

# 输入年份判断是不是闰年
year = int(input('请输入年份： '))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)
