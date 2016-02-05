#! /usr/bin/env python
# coding: utf-8

'''
使用round()函数，保留小数数位数
'''
o = round(1., 2)
print(o)

p = 3.1415926
o = round(p, 2)
print(o)

'''
当一个值刚好在左右选择的中间时，round函数的将舍入到最接近的偶数位
'''
o = round(1.5)
print(o)    # 2
o = round(2.5)
print(o)    # 2
o = round(3.5)
print(o)    # 4
o = round(4.5)
print(o)    # 4

'''
round函数的第二位也可以为负数，这样其代表舍入个位，十分位，百分位。
'''
o = round(63325, -1)
print(o)    # 63320
o = round(63325, -2)
print(o)    # 63300
o = round(63325, -3)
print(o)    # 63000

'''
format函数的舍入操作
'''
x = 1.23456
o = format(x, '0.2f')
print(o)    # 1.23
o = format(x, '0.3f')
print(o)    # 1.235
o = 'value is {:0.3f}'.format(x)
print(o)

