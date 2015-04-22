#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-04-20 16:22:32
# @About checkversion.py

try:
    import django
    print(django.get_version(), django.__path__)
except:
    print('No django has installed.')
    print('you can install the latest version using `sudo pip install django`')