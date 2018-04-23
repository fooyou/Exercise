#!/usr/bin/env python
# coding: utf-8
# @File Name: cycode.pyx
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-13 09:11:27
# @Last Modified: 2017-11-13 09:11:37
# @Description:

cdef void somethingElse():
    print("Away doing something else now...")

cdef public int myfunc() except *:
    cdef int retval = -1
    # do stuff...
    return retval

cdef public void run():
    try:
        myfunc()
        somethingElse()
    except Exception:
        print("Something wrong")

