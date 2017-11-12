#!/usr/bin/env python
# coding: utf-8
# @File Name: setup.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-12 14:11:47
# @Last Modified: 2017-11-12 14:11:18
# @Description:

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["primes.pyx"])
)
