#!/usr/bin/env python
# coding: utf-8
# @File Name: 10_memory_mapping_binary_files.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2016-02-17 12:02:03
# @Last Modified: 2016-02-17 20:02:28
# @Description:
'''
内存映射二进制文件至 mutable 字节数组。

使用 mmap 模块
'''

import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

SIZE = 10000

with open('./gzip_test.gz', 'wb') as f:
    f.seek(size=1)

