#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-03-18 16:55:34
# @About 2.1.Split_String_Multiple_Delimiters.py

line = 'asdf fjdk; afed, fjek,asdf,foo'
import re
fileds = re.split(r'[;,\s]\s*', line)
print(fileds)
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

fileds = re.split(r'(;|,|\s)\s*', line)
print(fileds)

# Getting the split characters might be useful in certain contexts. For example, maybe you
#need the split characters later on to reform an output string:
values = fileds[::2]
print(values)

delimiters = fileds[1::2] + ['']
print(delimiters)

# reform the line using the same delimiters
origin_str = ''.join(v + d for v, d in zip(values, delimiters))
print(origin_str)

# 既想使用小括号在正则中分组，又不想使用“捕获组”可以声明(?:...)
no_capture = re.split(r'(?:,|;|\s)\s*', line)
print(no_capture)