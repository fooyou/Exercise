#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: joshua
# @Date:   2015-05-23 20:06:31
# @Last Modified by:   Joshua Liu
# @Last Modified time: 2015-05-24 19:24:22

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 1, 'z': 4}
c = ChainMap(a, b)
print(c)

# 事实上ChainMap并没有真正把多个映射合成一个，而是通过逻辑重新定义了映射的常用操作
print(len(c))
print(list(c.keys()))
print(list(c.values()))

# 如果有重复的键值，将从第一个映射取值，所以c['z'] == a['z']，而不是等于b['z']
# 对合成映射c的操作只影响第一个映射a

c['z'] = 10
c['w'] = 40
del c['x']
print(a)

try:
    # 因为
    del c['y']
except Exception as e:
    print(e)

# ChainMap可以这样使用
# 
values = ChainMap()
values['x'] = 1
# 添加新映射
values = values.new_child()
values['x'] = 2
# 添加另外一个新映射
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
# 丢弃最后一个映射
values = values.parents
print(values)
values = values.parents
print(values)

# 也可以使用字典的update()方法来合并字典，如下：
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged)

# 这样可行，但它会创建一个完全独立的字典对象（或者改变其中一个字典）并且，如果任意一个原始字典改变了
# 并不会影响到合成的字典，如下：
a['x'] = 13
print(merged)

# 然而ChainMap使用原始的字典，所以它不会有上述行为，如下：
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged)
a['x'] = 13
print(merged)