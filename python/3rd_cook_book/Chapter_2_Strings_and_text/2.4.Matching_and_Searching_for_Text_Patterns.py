#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-08-27 16:58:48
# @About 2.4.Matching_and_Searching_for_Text_Patterns.py
#   对指定的式样进行匹配和搜索

text = 'yeah, but no, but yeah, but no, but yeah'

# 精确匹配
mat = text == 'yeah'
print(mat)  # False

# 匹配字符串开始或者结束
mat = text.startswith('yeah')
print(mat)  # True
mat = text.endswith('yeah')
print(mat)  # True

# 查找字符串中某个子串的第一次出现的位置
location = text.find('no')
print(location) # 10

'''
更复杂一些的匹配，可以使用re模块，比如匹配日期
'''

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

# 简单匹配：\d+ 表示匹配1个或多个数字
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
# yes

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
# no

'''
如果要发生多次匹配，那么就要创建一个式样对象。
'''
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
# yes

if datepat.match(text2):
    print('yes')
else:
    print('no')
# no

'''
match()方法总是去查找第一个匹配的字符，如果想搜索所有的匹配字符，可使用findall()：
'''
text = 'Today is 08/27/2015. PyCon starts 3/13/2013.'
results = datepat.findall(text)
print(results)  # ['08/27/2015', '3/13/2013']

'''
定义正则表达式时，一般会用括号来定义捕获分组：
'''
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

'''
捕获分组通常简化匹配的子匹配执行，因为每一分组可以独立的执行，例如：
'''
m = datepat.match('11/27/2012')
print(m)    # 

# 解析每一个分组
print(m.group(0))   # 11/27/2012
print(m.group(1))   # 11
print(m.group(2))   # 27
print(m.group(3))   # 2012
print(m.groups())   # ('11', '27', '2012')

# 查找所有匹配
print(datepat.findall(text))    # [('08', '27', '2015'), ('3', '13', '2013')]
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))
# 2015-08-27
# 2013-3-13

'''
findall() 返回所有匹配的结果，但对于大的文本来说，消耗会大。而finditer()可以迭代的返回每个数据，超赞的：
'''
for m in datepat.finditer(text):
    print(m.groups())
# ('08', '27', '2015')
# ('3', '13', '2013')



