#!/usr/bin/env python
# coding: utf-8
# @File Name: 11_multiple_sequences.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-02 10:02:04
# @Last Modified: 2016-02-02 11:02:03
# @Description:
'''
## 问题

如何同时遍历多个序列？

## 方案

使用内建的 zip() 函数，zip(a, b) 函数，内部创建一个 tuples(x, y)，x是a中的元素，y是b中的元素，遍历以短的那个序列长度结束。
'''

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

'''
输出如下：

1 101
5 78
4 37
2 15
10 62
7 99
'''

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    print(i)

'''
输出如下：

(1, 'w')
(2, 'x')
(3, 'y')

如果想以长的那个序列作为遍历的依据，可以使用 zip_longest() 代替：
'''

from itertools import zip_longest
for i in zip_longest(a, b):
    print(i)

'''
输出如下：

(1, 'w')
(2, 'x')
(3, 'y')
(None, 'z')


## 讨论

zip() 函数一般用于数据配对，比如 zip(a, b)。zip() 还可以传入多个序列，比如
'''

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = ['A', 'B', 'C']
for i in zip(a, b, c):
    print(i)

'''
输出如下：

(1, 'a', 'A')
(2, 'b', 'B')
(3, 'c', 'C')

最后，别忘了，zip() 函数产生了一个迭代器，如果想保存到列表里，得用 list() 函数
'''

print(zip(a, b))
print(list(zip(a, b)))
'''
<zip object at 0x7fae70412b08>
[(1, 'a'), (2, 'b'), (3, 'c')]
'''
