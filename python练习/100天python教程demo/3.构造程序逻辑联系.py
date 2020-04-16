#!/usr/local/bin/python3
# encoding:utf-8
'''
@File    :   3.构造程序逻辑联系.py
@Time    :   2020/04/09 14:33:11
@Author  :   WXL-c137
@Version :   1.0
@Contact :   844577557@qq.com
@WebSite :   null
'''
# Start typing your code from here

# 生成斐波那契数列：
""" list = [1, 1]
count = int(input('请输入数列长度'))

for i in range(count + 1):
    itme = list[i] + list[i + 1]
    list.append(itme)
 """
print(list)

# 找出10000以内的完美数。
""" class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False

        i, sum = 1, 0
        while i * i <= num:
            if num % i == 0:
                sum += i
            if i * i != num:
                sum += num / i
            i += 1

        return sum - num == num
 """

# 寻找水仙花数
""" for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num) """

# 百钱百鸡问题
""" for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z)) """

from random import randint

money = 1000

while money > 0:
    print('你的资产为：', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜！🎉')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜')
                money -= debt
            elif current == first:
                print('玩家胜')
                money += debt
            else:
                needs_go_on = True
print('你破产了，游戏结束！😥')