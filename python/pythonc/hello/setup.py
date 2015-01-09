#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: joshua
# @Date:   2014-11-13 14:52:44
# @Last Modified by:   joshua
# @Last Modified time: 2014-11-17 13:07:13

from distutils.core import setup, Extension

module1 = Extension('hello',
    # include_dirs=['/usr/local/include', '/opt/ffmpeg_build/include'],
    # library_dirs=['/opt/ffmpeg_build/lib', '/usr/local/lib'],
    # libraries=['avformat', 'avcodec', 'avutil'],
    sources=['hello.c'])

setup(name='PackageName',
    version='1.0',
    description='This package can analyze audio wave form.',
    ext_modules=[module1])
