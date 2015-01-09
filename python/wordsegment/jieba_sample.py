#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2014-12-05 17:21:12
# @About jieba_sample.py

import sys
import os
import jieba

a = "abcd"
print(",".join(a))

words = jieba.cut("结婚的和尚未结婚的")
print(" ".join(words))

