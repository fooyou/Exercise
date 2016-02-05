#!/usr/bin/env python
# coding: utf-8
# @File Name: 12_itertools_chain.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-02 11:02:11
# @Last Modified: 2016-02-02 14:02:58
# @Description:
from itertools import chain

a = [1, 2, 3, 4, 5]
b = ['x', 'y', 'z']

for x in chain(a, b):
    print(x)

'''
不好的写法： for x in a + b:    性能不好。
推荐的写法： for x in chain(a, b):
'''

print('\n')
for x in a + b:
    print(x)
