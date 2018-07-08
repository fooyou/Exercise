#!/usr/bin/env python
# coding: utf-8
# @File Name: test.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-04-20 14:04:20
# @Last Modified: 2018-04-20 14:04:15
# @Description:
from ctypes import *


class IP(Structure):
    _fields_ = [
        ("ihl", c_ubyte, 4),
        ("version", c_ubyte, 4),
        ("tos", c_ubyte),
        ("len", c_ushort),
        ("id", c_ushort),
        ("offset", c_ushort),
        ("ttl", c_ubyte),
        ("protocol_num", c_ubyte),
        ("sum", c_ushort),
        ("src", c_uint),
        ("dst", c_uint)
    ]

class Empty(Structure):
    _fields_ = []

print(sizeof(IP))
print(sizeof(Empty))
