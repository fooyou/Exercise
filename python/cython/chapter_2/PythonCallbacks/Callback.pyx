#!/usr/bin/env python
# coding: utf-8
# @File Name: Callback.pyx
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-11 10:11:58
# @Last Modified: 2017-11-11 10:11:54
# @Description:
cdef public:
    ctypedef void (*callback)(int)


cdef callback GlobalCallback


cdef public void SetCallback(callback cb):
    global GlobalCallback
    GlobalCallback = cb


cdef public void Notify(int value):
    global GlobalCallback
    if GlobalCallback != <callback>0:
        GlobalCallback(value)
