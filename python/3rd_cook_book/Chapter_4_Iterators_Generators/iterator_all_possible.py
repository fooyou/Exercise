#!/usr/bin/env python
# coding: utf-8
# @File Name: itertator_all_possible.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-01 13:02:37
# @Last Modified: 2016-02-02 10:02:05
# @Description:
'''
## 问题

如何列出一个序列的所有排列与组合


## 方案

排列：itertools.permutations()， 组合 itertools.combinations()
'''

items = ['China', 'Bratain', 'USA']
from itertools import permutations
for p in permutations(items):
    print(p)

'''
输出如下：

```
('China', 'Bratain', 'USA')
('China', 'USA', 'Bratain')
('Bratain', 'China', 'USA')
('Bratain', 'USA', 'China')
('USA', 'China', 'Bratain')
('USA', 'Bratain', 'China')
```

还可以通过自动选择排列个数，通过第二个参数
'''
print()

for p in permutations(items, 2):
    print(p)

'''
输出如下：

```
('China', 'Bratain')
('China', 'USA')
('Bratain', 'China')
('Bratain', 'USA')
('USA', 'China')
('USA', 'Bratain')
```
'''

from itertools import combinations
print('\n3元素组合：')
for c in combinations(items, 3):
    print(c)

print('\n2元素组合：')
for c in combinations(items, 2):
    print(c)

print('\n1元素组合：')
for c in combinations(items, 1):
    print(c)

'''
可以看到，这样的组合没有重复的元素，要有重复的元素，需要用到 combinations_with_replacement()
'''

from itertools import combinations_with_replacement
print('\n可重复的组合')
for c in combinations_with_replacement(items, 3):
    print(c)

'''
## 讨论

当然你可以自己写排列与组合，但是肯定得需要一定的精力和时间，所以还是优先考虑 itertools 吧。
'''
