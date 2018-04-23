import itertools

naturenum = itertools.count(1)  # 无限迭代器输出1的叠加数字
# for n in naturenum:
#     print(n, end=',')
naturerepeat = itertools.repeat('ABCD', 10)  # 无限迭代器重复迭代
# for m in naturerepeat:
#     print(m, end=',')

naturecycle = itertools.cycle("ABCD")  # 无限迭代器无限重复迭代对象数据
# for h in naturecycle:
#     print(h, end=',')

naturechain = itertools.chain("ABC", "DEF", "XYZ")  # 串联迭代器用户将可迭代对象进行串联输出
# for i in naturechain:
#     print(i, end=',')


naturegroudby = itertools.groupby("AAABBBCCCADDDXXXZZZBBBaavvAccdd", lambda a: a.upper())  # 分组迭代器用于迭代挑选重复的数据(连续的)
for j, group in naturegroudby:
    print(j, list(group))
