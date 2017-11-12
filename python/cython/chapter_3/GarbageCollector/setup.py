#!/usr/bin/env python
# coding: utf-8
# @File Name: setup.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-12 13:11:58
# @Last Modified: 2017-11-12 14:11:07
# @Description:

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension("PyData",
        ["PyData.pyx"])
]

setup(
    ext_modules = cythonize(ext_modules)
)
