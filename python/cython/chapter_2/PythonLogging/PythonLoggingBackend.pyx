#!/usr/bin/env python
# coding: utf-8
# @File Name: PythonLoggingBackend.pyx
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-11 11:11:29
# @Last Modified: 2017-11-11 11:11:26
# @Description:

import logging

cdef public void initLoggingWithLogFile(const char* logfile):
    logging.basicConfig(filename=logfile,
            level=logging.DEBUG,
            format='%(levelname)s %(asctime)s: %(message)s',
            datefmt='%Y-%m-%d %I:%M:%S')


cdef public void python_info(const char* message):
    logging.info(message)


cdef public void python_debug(const char* message):
    logging.debug(message)


cdef public void python_error(const char* message):
    logging.error(message)
