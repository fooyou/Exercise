#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2016-07-11 15:27:57
# @About yield_len.py: 

a = [1, 2, 3, 4, 5, 6]

def enum_yield(a):
    for i in a:
        yield i

if __name__ == '__main__':
    print(len(enum_yield(a)))