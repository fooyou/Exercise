#!/usr/bin/env python
# coding: utf-8
# @File Name: progress.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-07-13 10:07:12
# @Last Modified: 2016-07-13 13:07:57
# @Description:
import sys
import time
import threading
from queue import Queue

def progress(width, percent):
    print("[%s] %d%%" % (('%%-%ds' % width) % (percent * '='), percent), end='\r') 
    if percent >= 100:
        print()
        sys.stdout.flush()


if __name__ == '__main__':
    print('总进度:')
    for i in range(100):
        progress(100, (i + 1))
        time.sleep(0.05)
