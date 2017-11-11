#!/usr/bin/env python
# coding: utf-8
# @File Name: setup.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-11 21:11:45
# @Last Modified: 2017-11-11 22:11:50
# @Description:

from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

ext_modules = [
    Extension('mycodepy',
        ['mycodepy.pyx', 'mycode.c'])
]

setup(
    ext_modules = cythonize(ext_modules)
)
