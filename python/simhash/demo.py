#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-02-11 12:32:00
# @About demo.py

# import re
from simhash import Simhash
from simhash import SimhashIndex

data = {
    1: u'我 说 人 在 北京 还是 在 上海？',
    2: u'我 说 人 在 北京 还是 在 上海 呢？',
    3: u'This is simhash test.',
}
objs = [(str(k), Simhash(v)) for k, v in data.items()]
index = SimhashIndex(objs, k=4)
z = index.get_near_dups(Simhash(u'我 说 人 在 北京 还是 在'))
print(z)

# 对于汉语无论分词于不分词，simhash的结果是相同的。
# 
# x = Simhash('我说人在北京还是在上海？')
y = Simhash('hello')
x = Simhash('Hi')
# y = Simhash('我 说 人 在 北京 还是 在 上海 呢？')
print(x._features, x.value)
print(y._features, y.value)
print(x.distance(y))

xv = float(x.value) / float(y.value)
print(xv)
