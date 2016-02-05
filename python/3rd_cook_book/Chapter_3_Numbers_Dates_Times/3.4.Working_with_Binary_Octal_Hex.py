#! /usr/bin/env python
# coding: utf-8

'''
把整形数转换成二进制，八进制，十六进制，用到函数bin(), oct(), hex()
'''

x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

'''
还可以使用format函数
'''
o = format(x, 'b')
print(o)
o = format(x, 'o')
print(o)
o = format(x, 'x')
print(o)

'''
针对有符号的负数，format后也带负数
'''
x = -1234
o = format(x, 'b')
print(o)
o = format(x, 'x')
print(o)

'''
对于无符号数，需要加一个最大值来设置字节长度，比如一个32字节的无符号值，如下：
'''
o = format(2**32 + x, 'b')
print(o)
o = format(2**32 + x, 'x')
print(o)

'''
还可以使用int()函数来进行十进制转化
'''
o = int('4d2', 16)
print(o)

o = int('10011010010', 2)
print(o)

