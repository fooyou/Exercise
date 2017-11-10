#!/usr/bin/env python
# coding: utf-8
# @File Name: setup.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-10 18:11:32
# @Last Modified: 2017-11-10 21:11:06
# @Description:

from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

ext_modules = [
    Extension("PyAddFunction",
        ["PyAddFunction.pyx", "mathlib/src/AddFunction.c"],
        include_dirs=['mathlib/include'])
]

setup(
    ext_modules = cythonize(ext_modules)
)
