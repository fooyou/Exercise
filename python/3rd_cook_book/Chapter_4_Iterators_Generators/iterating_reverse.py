#!/usr/bin/env python
# coding: utf-8
# @File Name: iterating_reverse.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-01-28 10:01:53
# @Last Modified: 2016-01-28 11:01:31
# @Description:
'''
## Problem

    迭代翻转的序列
    You want to iterate in reverse over a sequence.

## Solution:
    使用reversed() 内建函数
    Use the build-in reversed() function. For example:
'''

a = [1, 2, 3, 4]

for x in reversed(a):
    print(x)

'''
反序迭代只适用于有固定大小的或者实现了 __reversed__() 函数对象，如何一个序列对象不满足以上任意一个条件，那么就需要把对象转换成 list， 比如以下代码：
'''

# 反序打印一个文件
f = open('/etc/passwd')
for line in reversed(list(f)):
    print(line, end='')

'''
请注意，把一个可迭代的序列转化成 list 可能消耗掉大量的内存。

## 讨论

许多程序员没有意识到逆序迭代可以在类中自定义实现，只要实现 __reversed__() 方法即可，如下代码：
'''

class Countdown:
    def __init__(self, start):
        self.start = start
    # 正向迭代
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    # 逆向迭代
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

a = Countdown(10)
for n in reversed(a):
    print(n, end='')
for n in iter(a):
    print(n, end='')

'''
定义逆向迭代使得代码更有效率，并且还无需在将数据转换成 list 再迭代。
'''
