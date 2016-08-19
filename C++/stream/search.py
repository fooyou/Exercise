#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2016-08-10 11:04:28
# @About search.py

import re

if __name__ == '__main__':
    keywords = ['国民党', '国 民  党', '国*民*党', '国-民_党', '国 Min 党']
    lines = []
    with open('data.txt', 'r') as f:
        for i, line in enumerate(f):
            lines.append((i, line))

    for key in keywords:
        print('search key:', key)
        for i, line in lines:
            if re.sub(r'[^\u4e00-\u9fa5a-zA-Z]', '', key).upper() in re.sub(r'[^\u4e00-\u9fa5a-zA-Z]', '', line).upper():
                print('    ln: %d  %s' % (i, line))
