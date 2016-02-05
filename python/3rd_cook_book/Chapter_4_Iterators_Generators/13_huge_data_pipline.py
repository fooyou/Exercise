#!/usr/bin/env python
# coding: utf-8
# @File Name: 13_huge_data_pipline.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-02 14:02:56
# @Last Modified: 2016-02-02 15:02:25
# @Description:
'''
## 问题

有很巨大的数据，内存都装不下，如何用 pipline 处理数据呢？

    foo/
       access-log-012007.gz
       access-log-022007.gz
       access-log-032007.gz
       ...
       access-log-012008
    bar/
       access-log-092007.bz2
       ...
       access-log-022008

## 方案

使用产生器函数
'''
import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    '''

    '''
    for path, dirs, files in os.walk(top):
        for fl in fnmatch.filter(files, filepat):
            yield os.path.join(path, fl)

def gen_opener(files):
    for fl in files:
        if fl.endswith('.gz'):
            f = gzip.open(fl, 'rt')
        elif fl.endswith('.bz2'):
            f = bz2.open(fl, 'rt')
        else:
            f = open(fl, 'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


lognames = gen_find('*.*', '~/Downloads')
for x in lognames:
    print(x)
files = gen_opener(lognames)
for fl in files:
    print(fl)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)
