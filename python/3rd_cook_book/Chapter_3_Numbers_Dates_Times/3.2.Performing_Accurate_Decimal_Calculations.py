#! /usr/bin/env python
# coding: utf-8

'''
如何忽略十进制float数的边界小问题
'''
a = 4.2
b = 2.1
print(a + b)

from decimal import Decimal
a = Decimal('1.3')
b = Decimal('1.7')
print(a + b)
print(a / b)

from decimal import localcontext

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

