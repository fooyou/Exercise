#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-04-02 17:13:36
# @About cairo_svg.py

import cairo
fo = open('test.svg', 'w')
W, H = 400, 250
surface = cairo.SVGSurface(fo, W, H)
ctx = cairo.Context(surface)
ctx.scale(W/1.0, H/1.0)
ctx.move_to(0.05, 0.4)
ctx.set_font_size(0.4)

ctx.show_text('Jekyll')
ctx.move_to(0.1, 0.8)
ctx.show_text('blog')

surface.finish()
fo.close()