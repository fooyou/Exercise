#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua Liu
# @Date:   2015-06-20 12:26:54
# @Last Modified by:   Joshua Liu
# @Last Modified time: 2015-06-20 13:08:20
#   查找替换大小写敏感的文本

import re

# 使用 re.IGNORECASE 来做操作，如下：
text = 'UPPER PYTHON, lower python, Mixed Python'
results = re.findall('python', text, flags=re.IGNORECASE)
print(results)
### ['PYTHON', 'python', 'Python']

substitution = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(substitution)
### UPPER snake, lower snake, Mixed snake

# 然而这种做法，有一个限制，替换文本不能匹配已经匹配的文本，如果要这样做，可以使用定制化函数
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

fi = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(fi)

