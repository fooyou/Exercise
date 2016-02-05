#!/usr/bin/env python
# coding: utf-8
# @File Name: 4_binary_file.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-04 13:02:02
# @Last Modified: 2016-02-04 14:02:35
# @Description:
'''
读写二进制文件，比如一张图片、音乐或者视频等。
'''
# 读取整个文件到一个单字节字符串
with open('/usr/bin/zip', 'rb') as f:
    data = f.read()

# 写二进制数据到文件
with open('binary.bin', 'wb') as f:
    f.write('床前明月光，疑是地上霜'.encode('utf-8'))

'''
读取二进制时，要知道返回的是字节字符串（byte strings），而不是文本字符串（text strings），同样，当写二进制数据至文件时，你必须提供字节数据。（比如：字节字符串，字节数组对象等等）

如何明了的知道文本字符串和字节字符串的区别呢？请看下面的代码：
'''

# 文本字符串
t = 'Hello World!'
print(t[0])
for c in t:
    print(c)

'''
H
H
e
l
l
o

W
o
r
l
d
!
'''

# 字节字符串
b = b'Hello World!'
print(b[0])
for c in b:
    print(c)

'''
72
72
101
108
108
111
32
87
111
114
108
100
33


所以只要你从二进制文件读写文本时，一定要记住要编解码 encode 或 decode。 例如：
'''

with open('binary.bin', 'rb') as f:
    data = f.read()
    print(data)
    text = data.decode('utf-8')
    print(text)


'''
另外关于二进制 I/O 的一个不太为人知道的方面是，像数组和 C 结构体这样的对象可以直接二进制写而不用做什么转换，看下面代码：
'''

import array
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin', 'wb') as f:
    f.write(nums)

'''
所有实现了被称作“buffer interface”的对象，都可以这样直接二进制写，“buffer interface”暴露了一块可直接用于二进制读写的内存缓冲区。

许多对象也支持直接把二进制数据通过 readinto() 方法读取到他们的存储结构中，看下面的代码：
'''

a = array.array('i', [1, 1, 1, 1, 1, 1])
print(a)
with open('data.bin', 'rb') as f:
    f.readinto(a)
print(a)

'''
然而，这样使用必须十分的小心，因为通常都要指定平台并且可能要依赖词的大小和字节排序，可参见5.9 读取二进制数据到 mutable 缓存。
'''
