#!/usr/bin/env python
# coding: utf-8
# @File Name: 16_infinite_loop.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-02 16:02:06
# @Last Modified: 2016-02-03 10:02:17
# @Description:
'''
要产生个死循环，会用 while(True)，如何用迭代器替换呢？

以下代码是常用的 while 系死循环：

CHUNKSIZE = 8192
def reader(s):
    while(True):
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


可以用 iter() 系代替：

def reader(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
    process_data(data)

内建的 iter() 函数的一个鲜为人知的特性是它选择性的接受一个无参数的回调函数和终结值作为输入。这么用时，它创建一个迭代器并不断的调用回调函数直到终结值时结束。

这对某种需要重复调用的函数非常有用，比如I/O读取。
'''
