#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua Liu
# @Date:   2015-05-24 19:32:07
# @Last Modified by:   Joshua Liu
# @Last Modified time: 2015-05-24 19:55:09
'''
fnmatch模块提供了2个函数：fnmatch()和fnmatchcase()来做Unix shell类似的通用匹配，
比如：*.py Dat[0-9] *.csv, 等等
'''

# 它的使用很简单：

from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
namelist = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(namelist)

# 通常，fnmatch()使用操作系统下文件系统的大小写敏感规则匹配式样，也就是大小写的匹配结果
# 要取决于操作系统，比如Mac OS 下下面的语句为False而在Windows下则为True
print(fnmatch('foo.txt', '*.TXT'))

# 如果有需要考虑大小写，请使用fnmatchcase()函数，它区分大小写：
print(fnmatchcase('foo.txt', '*.TXT'))

# 来看一个应用场景，假如从以下数据中找出一些地址：
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4082 N BROADWAY'
]
endwith_st = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(endwith_st)
begin_54_clark = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(begin_54_clark)