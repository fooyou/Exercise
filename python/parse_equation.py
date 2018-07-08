#!/usr/bin/env python
# coding: utf-8
# @File Name: parse_equation.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2018-05-31 17:05:51
# @Last Modified: 2018-05-31 17:05:50
# @Description:
import parser

eq = "blood_pressure > 140"
code = parser.expr(eq).compile()
blood_pressure = 141
print(code)
print(eval(code))

