#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-04-21 11:15:47
# @About hello.py

from flask import Flask
from flask import render_template
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    # return 'Hello World!'
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/response')
def response():
    response = make_response('<h1>This document carries a cookie!</h>')
    response.set_cookie('answer', '42')
    return response

if __name__ == '__main__':
    app.run(debug=True)