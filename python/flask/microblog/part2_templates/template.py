#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-06-12 13:49:10
# @About template.py
#   如果不使用模板，可能会像这样实现一个标题。ugly不是吗，所以Flask提供了模板，
#   它可以动态的可扩展的渲染html网页。
#   Flask使用jinja2为模板。

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Joshua'} # fake user
    posts = [ # fake arrat of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in China!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
        title='Home',
        user=user,
        posts=posts)


if __name__ == '__main__':
    app.run()
