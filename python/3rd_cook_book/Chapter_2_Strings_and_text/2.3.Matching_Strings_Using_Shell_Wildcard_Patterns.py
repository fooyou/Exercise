#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-08-27 15:54:08
# @About 2.3.Matching_Strings_Using_Shell_Wildcard_Patterns.py: 
#   怎么匹配Shell类似的“*.py”，“Dat[0-9]*.csv”等？

'''
fnmatch模块提供了两个函数：fnmatch()和fnmatchcase()，可用来match Shell Wildcard 式样。
'''

from fnmatch import fnmatch, fnmatchcase
mat = fnmatch('foo.txt', '*.txt')
print(mat)  # True

mat = fnmatch('foo.txt', '?oo.txt')
print(mat)  # True

mat = fnmatch('Dat45.csv', 'Dat[0-9]*')
print(mat)  # True

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
mat = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(mat)

'''
通常，fnmatch()匹配式样的大小写敏感规则和系统的文件系统是一样的。
'''

# On OS X (Mac)
mat = fnmatch('foo.txt', '*.TXT')
print(mat)  # False

# On Windows
mat = fnmatch('foo.txt', '*.TXT')
print(mat)  # True

'''
如果这个需要区分，那么使用大小写敏感的fnmatchcase()
'''

mat = fnmatchcase('foo.txt', '*.TXT')
print(mat)  # False     在任意OS上

'''
这个函数最被看中的是，它在处理非文件名字符上的潜力：
'''

addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
]

'''
你可以写出如下牛B的代码
'''

search_last_ST = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(search_last_ST)   # ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']

search_begin_54_with_CLARK = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(search_begin_54_with_CLARK)   # ['5412 N CLARK ST']



