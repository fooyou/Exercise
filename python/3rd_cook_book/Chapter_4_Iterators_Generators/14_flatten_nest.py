#!/usr/bin/env python
# coding: utf-8
# @File Name: 14_flatten_nest.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-02 15:02:35
# @Last Modified: 2016-02-02 16:02:23
# @Description:
'''
如何把一个折叠序列（nested sequence）铺展开来（flatten）？

使用迭代器函数和 isinstance() 函数。注意 yield from 的使用，它可以保证遍历所有的子序列。
'''
from collections import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)

items = ['PRC', ['EUR', 'IND', 'JAP'], 'USA', ['SPA', 'BRZ']]
for x in flatten(items):
    print(x)

'''
yield from 关键字是写叠加产生器函数的绝佳快捷途径，不过不用 yield from 的话，上述代码将会变成：
'''
def flatten_not_from(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten_not_from(x):
                yield i
        else:
            yield x

'''
虽然代码改动不大，但是 yield from 使得代码变得整洁容易阅读，但要知道 yield from 的用途不只这一点，在程序协同(coroutine)和基于产生器的并发性处理(concurrency)时，它也会大显身手的。关于其更多的信息参考12章12节。
'''
