#!/usr/bin/env python
# coding: utf-8
# @File Name: web.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-04 11:11:58
# @Last Modified: 2017-11-04 11:11:19
# @Description:
import os
from bottle import Bottle, static_file, run

HERE = os.path.abspath(os.path.dirname(__file__))
STATIC = os.path.join(HERE, 'static')

app = Bottle()


@app.route('/')
@app.route('/<filename:path>')
def serve(filename='index.html'):
    return static_file(filename, root=STATIC)


if __name__ == '__main__':
    run(app=app, host='localhost', port=8080)
