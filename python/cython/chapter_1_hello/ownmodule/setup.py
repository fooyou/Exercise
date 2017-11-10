#!/usr/bin/env python
# coding: utf-8
# @File Name: setup.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-10 18:11:32
# @Last Modified: 2017-11-10 19:11:15
# @Description:

from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

ext_modules = [
    Extension("PyAddFunction",
        ["PyAddFunction.pyx", "AddFunction.c"])
]

setup(
    ext_modules = cythonize("PyAddFunction.pyx")
)
