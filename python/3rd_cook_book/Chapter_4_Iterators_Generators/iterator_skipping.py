#!/usr/bin/env python
# coding: utf-8
# @File Name: iterator_skipping.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-01-29 11:01:01
# @Last Modified: 2016-01-29 18:01:06
# @Description:
'''
## 问题

如何丢弃迭代器的前面的部分数据？

```python
with open('./iterator_slice.py') as f:
    for line in f:
        print(line)
```

运行可以看到开头有很多注释，如何去掉这些注释呢？

## 方案

itertools 模块提供了一些函数能满足这种需求，先介绍一下 itertools.dropwhile() 函数。
'''
from itertools import dropwhile
with open('./iterator_slice.py') as f:
    for line in dropwhile(lambda line: line.startswith('#') or line.startswith("'''"), f):
        print(line, end='')

'''
还可以这么用，如果你确切的知道想略过去的行数。
'''

from itertools import islice
items = ['a', 'b', 'c', 1, 2, 66, 23]
for x in islice(items, 3, None):
    print(x)

'''
islice() 中的第三个参数为 None，意味着[3:]

## 讨论

dropwhile() 和 islice() 函数主要为避免如下的代码提供便利：
'''
with open('./iterator_skipping.py') as f:
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break
    while line:
        print(line, end='')
        line = next(f, None)

with open('./iterator_skipping.py') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')

with open('./iterator_skipping.py') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')


