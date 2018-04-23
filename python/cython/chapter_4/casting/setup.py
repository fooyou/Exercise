#!/usr/bin/env python
# coding: utf-8
# @File Name: setup.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-13 09:11:04
# @Last Modified: 2017-11-13 09:11:12
# @Description:
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("cycode.pyx", language="c++")
)
