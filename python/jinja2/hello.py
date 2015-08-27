#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-06-04 15:26:02
# @About hello.py

from jinja2 import Template

template = Template('Hello {{name}}')
print(template.render(name='Joshua'))