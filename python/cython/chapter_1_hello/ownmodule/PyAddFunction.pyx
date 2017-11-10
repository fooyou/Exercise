#!/usr/bin/env python
# coding: utf-8
# @File Name: PyAddFunction.pyx
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-10 18:11:01
# @Last Modified: 2017-11-10 18:11:05
# @Description:

cdef extern from "AddFunction.h":
    cdef int AddFunction(int, int)


def Add(a, b):
    return AddFunction(a, b)
