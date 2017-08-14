#!/usr/bin/env python
# coding: utf-8
# @File Name: test.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-08-02 10:08:56
# @Last Modified: 2017-08-04 17:08:37
# @Description:
import sys
import curses
from curses.textpad import Textbox, rectangle
from threading import Event

def hello():
    screen = curses.initscr()
    screen.border(1)
    screen.addstr(10, 27, str(h) + ' ' + str(w))
    screen.refresh()
    screen.getch()

    curses.COLOR_BLUE


def maxyx(screen):
    curses.use_default_colors()
    curses.init_pair(6, curses.COLOR_CYAN, -1)
    h, w = screen.getmaxyx()
    win = curses.newwin(h, w, 0, 0)
    s1 = '原谅我这一生不羁放纵爱自由'
    s2 = '也会怕有一天会跌倒'
    w1 = (len(s1) + len(s1.encode()))//2
    w2 = (len(s2) + len(s2.encode()))//2
    win.addstr(6, (w-w1)//2, s1)
    win.addstr(8, (w-w2)//2, s2, curses.color_pair(6))
    win.refresh()
    while True:
        ch = win.getch()
        if ord('q') == ch:
            break
        elif curses.KEY_RESIZE == ch:
            h, w = win.getmaxyx()
            win.clear()
            win.addstr(6, (w-len(s.encode()))//2, s)
            win.refresh()


def textbox(screen):
    screen.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)", curses.A_REVERSE)
    editwin = curses.newwin(5, 30, 2, 1)
    rectangle(screen, 1, 0, 1+5+1, 1+30+1)
    screen.refresh()

    box = Textbox(editwin)
    box.edit()

    message = box.gather()


if __name__ == '__main__':
    # hello()
    curses.wrapper(maxyx)
    # curses.wrapper(textbox)
