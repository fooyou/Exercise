# !/usr/bin/env python
# @File Name: colorconvert.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2016-10-19 14:10:31
# @Last Modified: 2016-10-19 17:10:51
# @Description:
# 
from colormath.color_objects import sRGBColor, CMYKColor
from colormath.color_conversions import convert_color

rgb = sRGBColor(0.1, 0.2, 0.3)
print(rgb)
cmyk = convert_color(rgb, CMYKColor)
print(cmyk)
