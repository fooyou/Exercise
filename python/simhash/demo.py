#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-02-11 12:32:00
# @About demo.py

# import re
from simhash import Simhash
from simhash import SimhashIndex
from data import news_lists_1, news_lists_2



# 对于汉语无论分词于不分词，simhash的结果是相同的。
# 
for i, news in enumerate(news_lists_1):
    x = Simhash(news_lists_1[i]['content'], f=64)
    #y = Simhash('hello')
    #x = Simhash('Hi')
    y = Simhash(news_lists_2[i]['content'], f=64)
    print('1.simhash:', x.value)
    print('2.simhash:', y.value)
    print('distance:', x.distance(y))
    print('similarity:', (64 - x.distance(y)) / 64)
    print(news_lists_1[i]['title'])

