#!/usr/bin/env python
# coding: utf-8
# @File Name: views.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-02-29 10:02:11
# @Last Modified: 2016-02-29 10:02:45
# @Description:
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

