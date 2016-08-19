#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2016-08-10 13:15:03
# @About test.py

import sys
import getopt
import re

if __name__ == '__main__':
    a = 'asd*c flkjg-fkgcd  _sd'
    print(re.sub(r'[^a]', '', a))