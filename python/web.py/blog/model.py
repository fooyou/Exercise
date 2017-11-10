#!/usr/bin/env python
# coding: utf-8
# @File Name: model.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-11-02 17:11:51
# @Last Modified: 2017-11-02 17:11:52
# @Description:
import web, datetime

db = web.database(dbn='sqlite', db='blog')

def get_posts():
    posts = db.select('entries', order='id DESC')
    new_posts = []
    for post in posts:
        post.posted_on = datetime.datetime.strptime(post.posted_on, '%Y-%m-%d %H:%M:%S')
        new_posts.append(post)
    return new_posts

def get_post(id):
    try:
        post = db.select('entries', where='id=$id', vars=locals())[0]
        post.posted_on = datetime.datetime.strptime(post.posted_on, '%Y-%m-%d %H:%M:%S')
        return post
    except IndexError:
        return None

def new_post(title, text):
    db.insert('entries', title=title, content=text, posted_on=datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

def del_post(id):
    db.delete('entries', where="id=$id", vars=locals())

def update_post(id, title, text):
    db.update('entries', where="id=$id", vars=locals(),
        title=title, content=text)
