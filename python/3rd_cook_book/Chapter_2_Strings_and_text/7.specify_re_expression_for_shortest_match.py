#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua Liu
# @Date:   2015-06-20 13:04:14
# @Last Modified by:   Joshua Liu
# @Last Modified time: 2015-06-20 13:31:24
#   为最短匹配指定正则表达式

import re
print(__name__)

str_pat = re.compile(r'\"(.*)\"')
text1 = 'compute says "no."'
results = str_pat.findall(text1)
print(results)
### ['no.']

text2 = 'Computer says "no." Phone says "yes."'
results = str_pat.findall(text2)
print(results)
### ['no." Phone says "yes.']

# 哦，看到问题了，我们想匹配的是封闭的""中的字符串，但是很明显example中的做不到，
# 如何做到呢：使用‘?’
#   使用“?”可以使匹配进入非贪婪模式，而执行最短匹配
#   “.”：可以匹配任意字符，except a newline(新行，不是\n)。使用括号括起来的"x.x"，如果指定开始和结束
# 将匹配最长可能的式样，在操作符（比如* +）右面加上"?"后，将匹配最短可能匹配。
str_pat = re.compile(r'\"(.*?)\"')
results = str_pat.findall(text2)
print(results)
### ['no.', 'yes.']