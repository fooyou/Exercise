#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-06-30 14:49:43
# @About views.py

from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    print('f: index')
    user = g.user
    posts = [{
        'author': {'nickname': 'Joshua'},
        'body': 'Beautiful day in Portland!'
    },{
        'author': {'nickname': 'Esther'},
        'body': 'The Aavengers movie was so cool!'
    }]
    return render_template('index.html',
            title='Home',
            user=user,
            posts=posts)

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    print('f: login')
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        print(form.openid.data)
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template("login.html",
                           title='Sign in',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@app.route('/logout')
def logout():
    print('f: logout')
    logout_user()
    return redirect(url_for('index'))

@lm.user_loader
def load_user(id):
    print('f: load_user')
    return User.query.get(int(id))

@oid.after_login
def after_login(resp):
    print('f: after_login')
    print(resp.email)
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email = resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.before_request
def before_request():
    print('f: before_request')
    g.user = current_user

@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    posts = [{
        'author': user, 'body': 'The post #1'
    }, {
        'author': user, 'body': 'The post #2'
    }]
    return render_template('user.html',
            user=user,
            posts=posts)