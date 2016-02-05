#!/usr/bin/env python
# coding: utf-8
# @File Name: 10_index_value.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-02 10:02:37
# @Last Modified: 2016-02-02 10:02:37
# @Description:
'''
## 问题

如何遍历一个序列，还想追踪序列的当前元素的索引值

## 方案

使用内建的 enumerate() 函数
'''

m_list = ['China', 'USA', 'Europe']
for idx, val in enumerate(m_list):
    print(idx, val)

'''
如果不从0开始，而从指定的值开始，可以填入第二个参数。
'''
print('\n')
for idx, val in enumerate(m_list, 1):
    print(idx, val)

'''
一个应用场景
'''

def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))

# parse_data('/etc/passwd')

data = [(1, 2), (3, 4), (5, 6), (7, 8)]
for n, (x, y) in enumerate(data):
    print(n, x, y)

try:
    for n, x, y in enumerate(data):
        print(n, x, y)
except Exception as e:
    print(e)
