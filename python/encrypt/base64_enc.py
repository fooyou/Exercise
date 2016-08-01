#!/usr/bin/env python
# coding: utf-8
# @File Name: base64_enc.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-08-01 10:08:34
# @Last Modified: 2016-08-01 10:08:24
# @Description:
import base64

bs = 'SouthChinaSea'
print(bs)
enc = base64.encodestring(bs.encode('utf-8'))
print(enc)
dec = base64.decodestring(enc)
dec = dec.decode('utf-8')
print(dec)
