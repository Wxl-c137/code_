""" 练习1：实现计算求最大公约数和最小公倍数的函数。 """
""" 找到能被x整除且能被y整除的最大的数
先确定x,y哪个更大
然后从挨个除，寻找能整除的数 """

// code
def(x, y):
    (x, y) = (y, x) if x > y else(x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
