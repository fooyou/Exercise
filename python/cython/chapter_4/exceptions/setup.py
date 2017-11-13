#!/usr/bin/env python
# coding: utf-8
# @File Name: setup.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-13 10:11:41
# @Last Modified: 2017-11-13 10:11:15
# @Description:

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("cycode",
        ["cycode.pyx", "main.c"])
)
