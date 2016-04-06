#!/usr/bin/env python
# coding: utf-8
# @File Name: 10_memory_mapping_bin_files.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-03-29 16:03:22
# @Last Modified: 2016-03-29 17:03:50
# @Description:
#   如何把二进制文件内存映射到 mutable 字节数组中？ mmap 模块

import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

size = 10
with open('10_data.bin', 'wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')

m = memory_map('10_data.bin')
print(len(m))
print(m[0 : size - 1])
print(m[0])

s = b'Hey you'
print(len(s))
m[0 : len(s) - 1] = s
m.close()

with open('10_data.bin', 'rb') as f:
    print(f.read(size))
