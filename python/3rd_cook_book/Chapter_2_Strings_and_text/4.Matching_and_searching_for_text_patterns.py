#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua Liu
# @Date:   2015-05-25 19:18:10
# @Last Modified by:   Joshua Liu
# @Last Modified time: 2015-06-20 12:25:42
#       文本匹配

text = 'yeah, but no, but yeah, but no, but yeah'

# 完全匹配
print(text == 'yeah')

# 匹配开始和结束
print(text.startswith('yeah'))
print(text.endswith('yeah'))

# 查找text中第一个匹配上得位置
print(text.find('no'))

'''
使用re正则做更精准的匹配
'''
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
# 简单匹配：\d+ 匹配一个或者多个数字
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# 使用Pattern对象匹配多个文本
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

# match() 先从字符串开始查找匹配，可用findall()匹配所有的字符片段
text = 'Today is 11/27/2012. PuCon starts 3/13/2013.'
print(datepat.findall(text))

# 分组
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m)

# 解析每个group
print(m.group(0)) # 11/27/2012
print(m.group(1)) # 11
print(m.group(2)) # 27
print(m.group(3)) # 2012
print(m.groups()) # ('11', '27', '2012')

month, day, year = m.groups()
print(datepat.findall(text))

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))


#
# re.sub() 使用介绍
# 

# 把 11/27/2012 => 2012-11-27
formdate = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text);
print(formdate) # Today is 2012-11-27. PuCon starts 2013-3-13.

# 当然如果有重复的操作可以这样：
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
formdate = datepat.sub(r'\3-\1-\2', text)
print(formdate)

# 更复杂的情况使用替换函数进行字符串替换 
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
formdate = datepat.sub(change_date, text)
print(formdate) # Today is 27 Nov 2012. PuCon starts 13 Mar 2013.

# 如果想知道共替换了多少个字符串，可以使用 re.subn()
formdate, n = datepat.subn(r'\3-\1-\2', text)
print(n)
