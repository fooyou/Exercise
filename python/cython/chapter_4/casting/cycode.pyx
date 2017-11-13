#!/usr/bin/env python
# coding: utf-8
# @File Name: cycode.pyx
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-13 09:11:30
# @Last Modified: 2017-11-13 09:11:37
# @Description:

cdef class foobar:
    pass

cdef class A:
    pass

cdef class B:
    pass

cdef A class1 = A()
cdef B class2 = B()
cdef B x = <B?> class1

