#! /usr/bin/env python
# coding: utf-8

'''
float类型的正无穷和负无穷和无效值
'''
import math

a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c)
print(math.isinf(a))
print(math.isnan(c))

