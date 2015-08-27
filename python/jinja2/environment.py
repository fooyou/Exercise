#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-06-04 15:29:28
# @About environment.py

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('jinja2', 'templates'))
template = env.get_template('mytemplate.html')