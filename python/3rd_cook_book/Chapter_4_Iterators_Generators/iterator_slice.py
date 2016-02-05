#!/usr/bin/env python
# coding: utf-8
# @File Name: iterator_slice.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-01-29 10:01:00
# @Last Modified: 2016-01-29 11:01:38
# @Description:
'''
## 问题

如何在迭代时取得切片数据？常规的切片操作不好使。

```python
def count(n):
    while True:
        yield n
        n += 1

c = count(0)

# 截取一段切片

slice = c[10:20]
```

运行代码，崩溃了

```
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'generator' object is not subscriptable
```

## 方案

使用 itertools.islice() 函数
'''

def count(n):
    while True:
        yield n
        n += 1

c = count(0)
import itertools
for x in itertools.islice(c, 10, 20):
    print(x)

'''
结果正是你想要的。

## 讨论

迭代器和生成器（Iterators 和 generators）不能正常的切片（slice），因为没有关于他们长度的信息（并且他们没有实现索引）。islice()的结果也是一个迭代器，不过它可以产出预定的切片子集，但却是耗费了所有的子集然后定位到切片开始，接下来的子集元素然后被 islice 对象逐个列举直到索引值结束。

值得强调的是 islice() 将在所提供的迭代器上消耗数据，然而迭代器是不能回溯的，考虑到这个因素，如果你想回溯的话，就先把数据变成 list 吧！
'''
