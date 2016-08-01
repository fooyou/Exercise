#!/usr/bin/env python
# coding: utf-8
# @File Name: vigenere.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-08-01 10:08:26
# @Last Modified: 2016-08-01 15:08:15
# @Description:
#   维吉尼亚密码,多表查询密码
#   表范围遵循 ASCII 0~255

import base64

def encrypt(string, key):
    encoded_chars = []
    for i, c in enumerate(string):
        key_c = key[i % len(key)]
        encoded_c = chr((ord(c) + ord(key_c)) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string.encode())

def decrypt(cipher, key):
    chars = []
    encoded_string = base64.urlsafe_b64decode(cipher).decode()
    for i, e in enumerate(encoded_string):
        key_c = key[i % len(key)]
        chrc = ord(e) - ord(key_c) if ord(e) - ord(key_c) >= 0 else ord(e) - ord(key_c) + 256
        c = chr(chrc)
        chars.append(c)
    string = ''.join(chars)
    return string

string = 'liuSY*&201607'
key = 'FuckYuenan'
print('string:', string)
enc = encrypt(string, key)
print('encrypt:', enc)
dec = decrypt(enc, key)
print('decrypt:', dec)
