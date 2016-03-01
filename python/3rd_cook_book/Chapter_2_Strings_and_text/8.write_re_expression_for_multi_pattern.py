#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua Liu
# @Date:   2015-06-20 13:26:04
# @Last Modified by:   Joshua Liu
# @Last Modified time: 2015-06-20 13:38:47

import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
            multiline comment */'''

result = comment.findall(text1)
print(result)
result = comment.findall(text2)
print(result)

# 哦，什么？text2 匹配不上？？
# 添加新行匹配的正则方法
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
result = comment.findall(text2)
print(result)
# 好了

# 还可以用 re.DOTALL 来激活'.'匹配新行
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
result = comment.findall(text2)
print(result)

# 关于 re.DOTALL 的更多的使用方法参见 2.18
