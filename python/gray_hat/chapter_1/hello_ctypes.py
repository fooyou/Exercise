#!/usr/bin/env python
# coding: utf-8
# @File Name: hello_ctypes.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-03-27 16:03:26
# @Last Modified: 2018-03-27 17:03:19
# @Description:
import os
from ctypes import *

class barley_amount(Union):
    _fields_ = [
        ("barley_long", c_long),
        ("barley_int", c_int),
        ("barley_char", c_char * 8)
    ]

value = input("Enter the amount of barley to put into the beer vat:")
my_barley = barley_amount(int(value))
print("Barley amount as a long: %ld" % my_barley.barley_long)
print("Barley amount as an int: %d" % my_barley.barley_int)
print("Barley amount as a char: %s" % my_barley.barley_char)

# 使用 nm 命令查看 dylib 的接口函数：nm -gU /usr/lib/libc.dylib

if os.name == 'posix':
    libc = cdll.LoadLibrary("libc.dylib")
    message_string = "Hello world!\n"
elif os.name == 'nt':
    pass
else:
    pass
