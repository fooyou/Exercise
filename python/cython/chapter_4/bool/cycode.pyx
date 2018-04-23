#!/usr/bin/env python
# coding: utf-8
# @File Name: cycode.pyx
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-13 09:11:46
# @Last Modified: 2017-11-13 09:11:51
# @Description:
from libcpp cimport bool

def run():
    cdef bool mybool = False
    print(mybool)

