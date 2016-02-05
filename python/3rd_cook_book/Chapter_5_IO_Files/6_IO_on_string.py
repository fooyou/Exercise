#!/usr/bin/env python
# coding: utf-8
# @File Name: 6_IO_on_string.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-05 10:02:23
# @Last Modified: 2016-02-05 10:02:47
# @Description:
'''
如何把文本或者二进制字符串写入类似文件对象的对象中？

使用 io.StringIO() 和 io.BytesIO() 类去创建类文件对象来操作字符串数据。
'''
import io

s = io.StringIO()
length = s.write('Hello World\n')
print(length)
print(s)
print('This is a test', file=s)

# 使用getvalue() 得到所有的数据
print(s.getvalue())

# 把现有字符串封装成类文件对象
s = io.StringIO('Hello\nWorld\n')
print(s.read(5))
print(s.read())

'''
io.StringIO() 只能用于文本，如果要操作二进制数据，就使用 io.BytesIO() 函数。
'''

s = io.BytesIO()
s.write('鸟鸣山更幽'.encode('utf-8'))
print(s.getvalue())

'''
io 模块的 StringIO() 和 BytesIO() 方法在你想要类文件对象的时候非常有用，比如在做单体测试时，你想模拟一个类文件对象的数据，因为你的代码只对文件对象有用。

要注意 StringIO() 和 BytesIO() 的实例没有合适的整形的文件描述。因此它们不能用于要求使用真实系统级的文件对象比如文件，管道或者 socket的代码。
'''
