#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-04-29 17:52:36
# @About test.py

from pycall import CallFile, Call, Application
call = Call('SIP/flowroute/13694182569')
action = Application('Playback', 'hello-world')
c = CallFile(call, action)
c.spool()