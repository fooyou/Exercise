#!/usr/bin/env python
# coding: utf-8
# @File Name: mycodepy.pyx
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-11 21:11:40
# @Last Modified: 2017-11-11 21:11:15
# @Description:

cdef extern from "mycode.h":
    struct mystruct:
        char* string
        int integer
        char** string_array
    void printStruct(mystruct*)


def testStruct():
    cdef mystruct s
    cdef char* array[2]
    s.string = "Hello World"
    s.integer = 2
    array[0] = "foo"
    array[1] = "bar"
    s.string_array = array
    printStruct(&s)

