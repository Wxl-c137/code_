# 练习1：实现计算求最大公约数和最小公倍数的函数。
x = int(input('请输入第一个数字'))
y = int(input('请输入第二个数字'))

z = int(input('请选择要进行的运算， 1: 求最大公约数， 2：求最小公倍数'))


def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print('最大公约数位%d' % factor)
            break


def lcm(x, y):
    lcmnum = x * y
    print('最小公倍数%d' % lcmnum)


if z == 1:
    gcd(x, y)
else:
    lcm(x, y)