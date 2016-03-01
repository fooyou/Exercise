#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-06-30 14:06:28
# @About __init__.py

from flask import Flask

app = Flask(__name__)
from app import views

