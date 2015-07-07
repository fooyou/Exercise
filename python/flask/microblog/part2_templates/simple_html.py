#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-06-12 13:49:10
# @About simple_html.py
#   如果不使用模板，可能会像这样实现一个标题。ugly不是吗，所以Flask提供了模板，
#   它可以动态的可扩展的渲染html网页。
#   本示例可以告诉你template是如何诞生的。

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Joshua'} # 占位对象，ugly!
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''


if __name__ == '__main__':
    app.run()
