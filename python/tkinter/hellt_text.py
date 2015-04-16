#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joshua
# @E-Mail: liuchaozhen@neusoft.com
# @Date:   2015-04-14 16:57:05
# @About hellt_text.py

from tkinter import *
from tkinter import ttk

root = Tk()
log = Text(root, state='disabled', width=80, height=24, wrap='none')
log.grid()

def writeToLog(msg):
    numlines = log.index('end - 1 line').split('.')[0]
    log['state'] = 'normal'
    if numlines==24:
        log.delete(1.0, 2.0)
    if log.index('end-1c')!='1.0':
        log.insert('end', '\n')
    log.insert('end', msg)
    log['state'] = 'disabled'