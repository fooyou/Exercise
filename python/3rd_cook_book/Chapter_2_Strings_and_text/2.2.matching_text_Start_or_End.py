#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-03-18 18:36:58
# @About 2.2.matching_text_Start_or_End.py

# Problem
# You need to check the start or end of a string for specific text patterns, such
# as filename extensions, URL schemes, and so on.
# 
# Solution
# A simple way to check the beginning or end of a string is to use the str.starts
# with() or str.endswith() methods. For example:

filename = 'spam.txt'
boolean = filename.endswith('.txt')
print(boolean)

boolean = filename.startswith('spool')
print(boolean)

url = 'http://www.python.org'
boolean = url.startswith('http:')
print(boolean)

# If you need to check against multiple choices, simply provide a tuple of
# possibilities to startswith() or endswith() :
import os
filenames = os.listdir('.')
print(filenames)
lst = [name for name in filenames if name.endswith(('.c', '.py'))]
print(lst)
boolean = any(name.endswith('.py') for name in filenames)
print(boolean)

# Here is another example:
from urllib import urlopen

def read_data(name):
    if name.startswith(('https:', 'http:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

# Oddly, this is one part of Python where a tuple is actually required as input. If you happen
# to have the choices specified in a list or set, just make sure you convert them using
# tuple() first. For example:
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
# url.startswith(choices)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: startswith first arg must be str or a tuple of str, not list
boolean = url.startswith(tuple(choices))
print(boolean)

# Discussion
# The startswith() and endswith() methods provide a very convenient way to perform
# basic prefix and suffix checking. Similar operations can be performed with slices, but
# are far less elegant. For example:
filename = 'spam.txt'
boolean = filename[-4:] == '.txt'
print(boolean)

url = 'http://www.python.org'
boolean = url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'
print(boolean)

# You might also be inclined to use regular expressions as an alternative. For example:
import re
url = 'http://www.python.org'
re.match('http:|https:|ftp:', url)

# This works, but is often overkill for simple matching. Using this recipe is simpler
# and runs faster.
# Last, but not least, the startswith() and endswith() methods look nice when com‐
# bined with other operations, such as common data reductions. For example, this state‐
# ment that checks a directory for the presence of certain kinds of files:
#   if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
#       ...