#!/usr/bin/env python
# coding: utf-8
# @File Name: setup.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-10 17:11:37
# @Last Modified: 2017-11-10 17:11:33
# @Description:
#   使用方法：
#   $ python setup.py build_ext --inplace
# 
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("helloworld.pyx")
)
