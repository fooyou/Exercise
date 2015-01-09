#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @Date:   2014-10-24 15:11:06
# @Last Modified by:   Joshua
# @Last Modified time: 2014-10-24 18:06:44
from distutils.core import setup, Extension

module1 = Extension('wavepoint',
    include_dirs=['/usr/local/include'],
    library_dirs=['/usr/local/lib'],
    libraries=['avformat', 'avcodec', 'avutil'],
    sources=['wavepoint.c'])

setup(name='PackageName',
    version='1.0',
    description='This package can analyze audio wave form.',
    ext_modules=[module1])