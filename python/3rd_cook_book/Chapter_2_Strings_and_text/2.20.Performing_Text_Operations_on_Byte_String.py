#! /usr/bin/env python
# coding: utf-8

'''
对byte字符串执行普通的文本操作
'''

data = b'Hello World'
o = data[0:5]
print(o)
o = data.startswith(b'Hello')
print(o)
o = data.split()
print(o)
o = data.replace(b'Hello', b'Hello Cruel')

'''
Bytearray
'''
data = bytearray(b'Hello World')
o = data[0:5]
print(o)
o = data.startswith(b'Hello')
print(o)
o = data.split()
print(o)
o = data.replace(b'Hello', b'Hello Joshua')
print(o)

'''
对byte字符串使用正则表达式的时候，需要对patern使用`b`
'''

data = b'FOO:BAR, SPAM'
import re
o = re.split(b'[:,]',data)
print(o)

'''
奶奶的，文本字符串和Byte字符串到底呦啥子不同啊？
绝大部分的针对文本字符串的操作对字节字符串都使用，但就其区别主要如下：
1. 对字节字符串的索引访问将返回整形数，而不是字符
'''
s = 'Hello World'
b = b'Hello World'
print(s[0], s[6])
print(b[0], b[6])

'''
2. 字节字符串打印不好看且需要decode才能干净呈现
'''

b = b'Hello World'
print(b)
print(b.decode('ascii'))

'''
3. 字符串格式化操作不能用于字节字符串
'''
try:
    b'%10s %10d %10.2f' % (b'ACME', 100, 490.1)
except Exception as e:
    print(e)

try:
    b'{} {} {}'.format(b'ACME', 100, 490.1)
except Exception as e:
    print(e)

'''
如果想对字节字符串格式化处理，则可以decode encode转换：
'''

o = '{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')
print(o)

