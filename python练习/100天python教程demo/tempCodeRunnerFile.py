if year % 4 == 0:
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