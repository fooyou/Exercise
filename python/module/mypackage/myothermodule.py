#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2014-11-28 18:34:36
# @About:  

from .mymodule import as_int

def add(a, b):
    return as_int(a) + as_int(b)

def _test():
    assert (add('1', '1') == 3)

if __name__ == '__main__':
    _test()