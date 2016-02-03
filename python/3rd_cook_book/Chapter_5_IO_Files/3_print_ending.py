#!/usr/bin/env python
# coding: utf-8
# @File Name: 3_print_ending.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-03 16:02:59
# @Last Modified: 2016-02-03 18:02:52
# @Description:
'''
print 函数打印不同的结束符
'''
print('中国', 56, 31)
# 中国 56 31

print('中国', 56, 31, sep=',')
# 中国,56,31

print('中国', 56, 31, sep=',', end='!!\n')
# 中国,56,31!!

for i in range(5):
    print(i)

# 0
# 1
# 2
# 3
# 4

for i in range(5):
    print(i, end=' ')

# 0 1 2 3 4 

print()

'''
假如 row = ('中国', 56, 32)，如何打印出 "中国,56,32"呢？
'''
row = ('中国', 56, 32)
print(','.join(str(x) for x in row))

'''
这种写法虽然也简单，但是不易阅读，大招来了
'''
print(*row, sep=',')

'''
*row 是什么东东，文章里没说，但据说 *代表一个序列，比如 set()，tuple()，而 **代表一个字典。
'''

