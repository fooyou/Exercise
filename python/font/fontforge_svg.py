#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-04-02 17:27:38
# @About fontforge_svg.py

import fontforge

f = fontforge.open('hanyizhuan.ttf')
g = f[u'君子博学而日参省乎己']
print(g)
g.export('gental.svg')