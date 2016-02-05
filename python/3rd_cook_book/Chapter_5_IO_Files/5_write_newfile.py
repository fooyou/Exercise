#!/usr/bin/env python
# coding: utf-8
# @File Name: 5_write_newfile.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-04 16:02:54
# @Last Modified: 2016-02-04 18:02:07
# @Description:
'''
只有当某个文件不存在时才写入数据到文件，使用 'x' 参数
'''

with open('data', 'xt') as f:
    f.wrte('大江东去浪淘尽，千古风流人物')

'''
若写的是二进制文件则使用 'xb'，文本文件用 'xt'，当然也可以这样写：
'''

import os
if not os.path.exists('data'):
    with open('data', 'wt') as f:
        f.wrte('大江东去浪淘尽，千古风流人物')

'''
'''
