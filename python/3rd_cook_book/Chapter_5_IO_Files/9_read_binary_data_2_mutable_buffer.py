#!/usr/bin/env python
# coding: utf-8
# @File Name: 9_read_binary_data_2_mutable_buffer.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-05 15:02:46
# @Last Modified: 2016-02-05 17:02:15
# @Description:
'''
PS：mutable: 易变的，不可靠的，和constant是反义词。

如何直接把二进制文件读取到一个可变的缓冲区中，而不要中间拷贝？

使用 readinto() 函数
'''

import os
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

with open('9.bin', 'wb') as f:
    f.write('数风流人物还看今朝！'.encode('utf-8'))

buf = read_into_buffer('9.bin')
print(buf)

buf[0:5] = b'NiuBee'
print(buf)

with open('9_new.bin', 'wb') as f:
    l = f.write(buf)
    print(l)

'''
file 的 readinto() 方法可以把文件数据填充到预先申请内存的数组里，甚至是使用 array 模块或者类如 numpy 创建的数组都可以填充。

不像通常的 read() 方法，readinto() 函数把文件数据填充到已申请好内存的缓冲里而不是新创建对象并返回。因此你可以用它来避免额外的内存申请。比如，你要等大小的读取一个文件，就可以这样写代码：
'''

record_size = 4
buf = bytearray(record_size)
with open('9.bin', 'rb') as f:
    while True:
        n = f.readinto(buf)
        print(buf, buf.decode('utf-8', 'ignore'))
        if n < record_size:
            break

