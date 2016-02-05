#! /usr/bin/env python
# coding: utf-8

'''
从字节字符串中解压出整形值，或者反向把超大整形数打包进字节字符串。
'''

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

'''
可使用int.to_bytes()来反向处理
'''
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

'''
struct模块的unpack函数
'''
import struct
hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)


'''
那么littile或者big的字节排序只是表明了低位到高位，还是高位到低位，下面例子可见：
'''
x = 0x01020304
print(x.to_bytes(4, 'big'))
# b'\x01\x02\x03\x04'
print(x.to_bytes(4, 'little'))
# b'\x04\x03\x02\x01'



