#!/usr/bin/env python
# coding: utf-8
# @File Name: 15_sort_merge.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-02 16:02:06
# @Last Modified: 2016-02-02 16:02:45
# @Description:
'''
假如有多个有序序列，如何得到其合并后的有序数列？
'''

import heapq

a = [1, 4, 7, 10]
b = [2, 5, 9, 11]
for c in heapq.merge(a, b):
    print(c)

a = [7, 4, 1, 10]
b = [2, 9, 5, 11]
for c in heapq.merge(a, b):
    print(c)

'''
这个函数看起来没什么特别的，但是它不会一下子读取所有的序列，这就意味着你可以用很小的代价就可以遍历超长超大的序列，假如有两个超大的文件，需要合并，就可以这么写出快捷的访问程序。
'''

with open('sorted_file_1', 'rt') as f1, \
        open('sorted_file_2', 'rt') as f2, \
        open('merged_file', 'wt') as fo:
            for line in heapq.merge(f1, f2):
                fo.write(line)

'''
但值得强调的是 heapq.merge() 的输入序列必须是有序的序列。以为它不会一下读取所有的序列元素到堆上，所以也不会对其进行排序，也不会检查数据是否是有序的
'''
