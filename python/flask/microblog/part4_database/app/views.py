#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-06-30 14:49:43
# @About views.py

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template("login.html",
                           title='Sign in',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
