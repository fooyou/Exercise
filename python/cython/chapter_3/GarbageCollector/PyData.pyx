#!/usr/bin/env python
# coding: utf-8
# @File Name: PyData.pyx
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-11 22:11:10
# @Last Modified: 2017-11-12 14:11:43
# @Description:

cimport PyData
from libc.stdlib cimport malloc, free

cdef class Data(object):
    cdef PyData.data_t* _nativeData

    def __init__(self, int value):
        self.SetValue(value)

    def __cinit__(self):
        self._nativeData = <data_t*>malloc(sizeof(data_t))
        if not self._nativeData:
            self._nativeData = NULL
            raise MemoryError()

    def __dealloc__(self):
        if self._nativeData is not NULL:
            free(self._nativeData)
            self._nativeData = NULL

    def __str__(self):
        if self._nativeData is not NULL:
            return "%s" % self.Value
        else:
            return "Object not initialized!"

    cdef SetNativeValue(self, int value):
        self._nativeData.value = value

    @property
    def Value(self):
        return self._nativeData.value

    def SetValue(self, int value):
        self.SetNativeValue(value)

