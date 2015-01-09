#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: joshua
# @Date:   2014-11-17 15:14:51
# @Last Modified by:   joshua
# @Last Modified time: 2014-11-18 20:09:04

import os
import re

# files = os.listdir('res')
# print(files)

# files.sort()
# for fl in files:
#     print(fl)

fileslist = ['0.0-52.73.wav.txt', '102.14-152.32.wav.txt', '152.32-180.0.wav.txt', '52.73-102.14.wav.txt']


fileslist.sort(key=lambda x : float(re.split('\-', x)[0]))
for fl in fileslist:
    # times = re.split('\-', fl)
    print(fl, re.split('\-', fl)[0])

# def make_repeater (n):
#     return lambda s: s*n

# twice = make_repeater(2)

# print(twice('word'))
# print(twice(5))

strtest = '0.0-52.73.wav.txt'
get_float = lambda x : re.split('\-', x)[0]
print(get_float(strtest))