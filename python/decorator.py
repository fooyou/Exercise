#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-07-17 15:59:49
# @About decorator.py

import sys
import getopt

'''
装饰函数的用法和语法：

1. 
@deco
def foo():
    pass

以上调用等同于：

foo = deco(foo)


2.
@deco1(deco_args)
@deco2
def foo():
    pass

等同于：

foo = deco1(deco_args)(deco2(foo))
'''

def log(func):
    def wrappedFunc():
        print('*** %s() is called' % func.__name__)
        return func()
    return wrappedFunc

@log
def foo():
    print('inside foo()')

if __name__ == '__main__':
    foo()